import jieba
import re
import operator
from gensim.models import Word2Vec

def getwordlist():
    model = Word2Vec.load("E:\SIGIR\Embedding/word_embedding")
    line = open('E:\SIGIR\证据类种子词库\百度百科.txt', 'r').readline()
    line = re.sub('[\s+\.\!\/_$%^*(+\"\')a-zA-Z0-9]+|[+——()?【】“”！。？、~@#￥%……&*（）]+', "", line)
    stop_words = [w.strip() for w in open('D:/success/ciku/chinese_stopword.txt').readlines()]
    wordlist = jieba.cut(line)
    wordlist = [w for w in wordlist if len(w) >= 2 and w not in stop_words]
    wordfrequency = {}
    for word in wordlist:
        if word not in wordfrequency.keys():
            wordfrequency[word] = 1
        else:
            wordfrequency[word] += 1
    wordfrequency = sorted(wordfrequency.items(), key=lambda x: x[1], reverse=True)
    wordset = []
    for item in wordfrequency:
        wordset.append(item[0])
    return wordset

def closewordset(model,wordset):
    sum = 0
    count = 0
    if len(wordset) == 1:
        return 0
    for i in range(0,len(wordset)):
        for j in range(i+1,len(wordset)):
            try:
                sum += model.similarity(wordset[i],wordset[j])
                count += 1
            except KeyError:
                sum +=0
    return sum
def rank(model,wordset):
    wordsimilar = {}
    for word in wordset:
        try:
            wordsimilar[word] = model.similarity('证据',word)
        except KeyError:
            continue
    wordsimilar = sorted(wordsimilar.items(), key=lambda x: x[1], reverse=True)
    wordset1 = []
    for item in wordsimilar:
        wordset1.append(item[0])
    return wordset1

def DVI(model,wordset1,wordset2):
    min = 10
    max = 0
    for word1 in wordset1:
        for word2 in wordset2:
            try:
                similar = model.similarity(word1, word2)
                if similar>0:
                    if min >= similar:
                        min = similar
            except KeyError:
                continue
    for i in range(0,len(wordset1)):
        for j in range(i+1,len(wordset1)):
            try:
                similar = model.similarity(wordset[i], wordset[j])
                if max <= similar:
                    max = similar
            except KeyError:
                continue
    print('min:'+str(min))
    print('max:' + str(max))
    return min/max


if __name__ == "__main__":
    model = Word2Vec.load("E:\SIGIR\Embedding/word_embedding")
    wordset = getwordlist()
    wordset = rank(model,wordset)
    print(wordset)
    resultlist1 = []
    resultlist3 = {}
    resultlist4 = []
    for word in wordset:
        resultlist2 = []
        resultlist1.append(word)
        for word1 in wordset:
            if word1 not in resultlist1:
                resultlist2.append(word1)
        close = closewordset(model,resultlist1) + closewordset(model,resultlist2)
        #close = model.n_similarity(resultlist1,resultlist2)
        print(word+' '+str(close))
        resultlist3[word] = close
    for i in range(0,len(wordset)-1):
        if resultlist3[wordset[i]] > resultlist3[wordset[i+1]]:
            resultlist4.append(wordset[i])
    f = open('E:\SIGIR\证据类种子词库\种子词库.txt','w')
    for word in resultlist4:
        f.write(word+'\n')
    f.close()