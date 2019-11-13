import jieba
from sklearn.cluster import AffinityPropagation
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
import numpy as np
import math
# AP聚类和Kmeans聚类

def getwords(event):#得到事件中的词
    model = Word2Vec.load("E:\SIGIR\Embedding/word_embedding")
    lines = open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
    stop_words = [w.strip() for w in open('D:/success/ciku/chinese_stopword.txt').readlines()]
    wordlist = []
    for line in lines:
        wordlists = jieba.cut(line)
        wordlists = [w for w in wordlists if w.replace('.', '').isdigit() is False and len(w) >= 2 and w not in stop_words]
        for word in wordlists:
            wordlist.append(word)
    wordfrequency = {}
    for word in wordlist:
        if word not in wordfrequency.keys():
            wordfrequency[word] = 1
        else:
            wordfrequency[word] += 1
    wordlist2 = []
    for word in wordlist:
        if word not in wordlist2 and wordfrequency[word] <=5:
            try:
                a = model[word]
                wordlist2.append(word)
            except KeyError:
                continue
    wordlist = wordlist2
    return wordlist

def normalize(word_vec):
    norm=np.linalg.norm(word_vec)
    if norm == 0:
     return word_vec
    return word_vec/norm

def wordsvector(word1,word2):#计算相似矩阵中的一个元素
    corewords = coreword()
    model = Word2Vec.load("E:\SIGIR\Embedding/word_embedding")
    basicvector = model['证据']
    word1vector = model[word1]
    word2vector = model[word2]
    basicvector = normalize(basicvector)
    word1vector = normalize(word1vector)
    word2vector = normalize(word2vector)
    cosword1 = np.dot(word1vector,basicvector)/(np.linalg.norm(word1vector)*np.linalg.norm(basicvector))
    cosword2 = np.dot(word2vector, basicvector) / (np.linalg.norm(word2vector) * np.linalg.norm(basicvector))
    degreeword1 = math.acos(cosword1)
    degreeword2 = math.acos(cosword2)
    degreeD = abs(degreeword1-degreeword2)
    cosdegreeD = math.cos(degreeD)
    return cosdegreeD




def wordmatrix(wordlist,model):#得到相似矩阵
    wordsmatrix = []
    for word in wordlist:
        wordsmatrix.append(model[word])
    return wordsmatrix


def AP(wordsmatrix):#AP聚类
    ap = AffinityPropagation(damping=0.5, max_iter=300, convergence_iter=30).fit(wordsmatrix)
    cluster_centers_indices = ap.cluster_centers_indices_
    lables = ap.labels_
    return cluster_centers_indices,lables

def Kmeans(wordsmatrix,k):#Kmeans聚类
    kmeans = KMeans(n_clusters=k, random_state=0).fit(wordsmatrix)
    cluster_centers_indices = kmeans.cluster_centers_
    lables = kmeans.labels_
    return cluster_centers_indices, lables

def coreword():#得到种子词库中的词
    corewords = []
    lines = open('E:\SIGIR\证据类种子词库\种子词库.txt', 'r').readlines()
    for line in lines:
        line = line.replace('\n', '')
        corewords.append(str(line))
    return corewords

def wordset(cluster_centers_indices,lables,wordlists):#得到聚类之后的结果
    num = len(cluster_centers_indices)
    wordsetsindexs = []
    for i in range(0,num):
        wordlist = []
        for j in range(0,len(lables)):
            if lables[j] == i:
                wordlist.append(j)
        wordsetsindexs.append(wordlist)
    wordsets = []
    for wordsetindex in wordsetsindexs:
        wordlist = []
        for i in wordsetindex:
            word = wordlists[i]
            wordlist.append(word)
        wordsets.append(wordlist)
    return wordsets


def similartocore(word,corewords,model):#得到一个词和种子词库之间的相似度
    sum = 0
    for coreword in corewords:
        sum += model.similarity(word,coreword)
    return sum/len(corewords)

def mostsimilarset(wordsets,corewords,model):#找到和种子词库最相似的词集
    wordsetscore = {}
    max = 0
    mostsimilarlist = []
    for wordset in wordsets:
        count = len(wordset)
        sum = 0
        for word in wordset:
            sum += similartocore(word,corewords,model)
        wordsetsim = sum/count
        #wordsetsim = sum
        if wordsetsim >= max and len(wordset)>=3:
            max = wordsetsim
            mostsimilarlist = wordset
    return mostsimilarlist

def getmostsimilarwordsAP(event):#AP聚类后找到和种子词库最相似的词集
    wordlist = getwords(event)
    model = Word2Vec.load("E:\SIGIR\Embedding/word_embedding")
    wordsmatrix= wordmatrix(wordlist,model)
    cluster_centers_indices, lables = AP(wordsmatrix)
    wordsets = wordset(cluster_centers_indices, lables, wordlist)
    corewords = coreword()
    mostsimilarlist = mostsimilarset(wordsets, corewords, model)
    # for word in corewords:
    #     if word not in mostsimilarlist:
    #         mostsimilarlist.append(word)
    return mostsimilarlist

def getmostsimilarwordsKmeans(event,k):#Kmeans聚类后找到和种子词库最相似的词集
    wordlist = getwords(event)
    model = Word2Vec.load("E:\SIGIR\Embedding/word_embedding")
    wordsmatrix = wordmatrix(wordlist,model)
    cluster_centers_indices, lables = Kmeans(wordsmatrix,k)
    wordsets = wordset(cluster_centers_indices, lables, wordlist)
    corewords = coreword()
    mostsimilarlist = mostsimilarset(wordsets, corewords, model)
    # for word in corewords:
    #     if word not in mostsimilarlist:
    #         mostsimilarlist.append(word)
    return mostsimilarlist

def getpandr(event,mostsimilarlist):#得到准确率和召回率
    sentimentindex = {}
    sentimentindex['产妇'] = [0, 1, 4, 6]
    sentimentindex['红黄蓝'] = [4, 9]
    sentimentindex['山东'] = [6, 8]
    sentimentindex['魏则西'] = [8, 9]
    lines = open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
    resultlist = []
    for i in range(0,len(lines)):
        for word in mostsimilarlist:
            if word in lines[i]:
                resultlist.append(i)
    p = 0
    resultlist2 = []
    for i in resultlist:
        if i not in resultlist2:
            resultlist2.append(i)
    resultlist = resultlist2
    for i in resultlist:
        print(lines[i])
    #print(resultlist)
    for i in resultlist:
        if i in sentimentindex[event]:
            p+=1
    precision = p/len(resultlist)
    r = 0
    for i in sentimentindex[event]:
        if i in resultlist:
            r+=1
    recall = r/len(sentimentindex[event])
    return precision,recall






if __name__ == "__main__":
    events = ['产妇','红黄蓝','山东','魏则西']
    for event in events:
        mostsimilarlist = getmostsimilarwordsAP(event)
        print(mostsimilarlist)
        print(getpandr(event,mostsimilarlist))
    print('\n')
    for event in events:
        mostsimilarlist = getmostsimilarwordsKmeans(event,15)
        print(mostsimilarlist)
        print(getpandr(event,mostsimilarlist))