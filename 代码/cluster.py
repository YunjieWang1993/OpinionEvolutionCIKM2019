import jieba
from gensim.models import Word2Vec

def getwords(event,model):#得到事件中的词
    lines = open('E:\SIGIR\事件新闻/' + event + '长新闻.txt', 'r').readlines()
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
        if word not in wordlist2 and wordfrequency[word]<=3:
            try:
                a = model[word]
                wordlist2.append(word)
            except KeyError:
                continue
    wordset = wordlist2
    return wordset

def coreword():#得到种子词库中的词
    corewords = []
    lines = open('E:\SIGIR\证据类种子词库\种子词库筛选.txt', 'r').readlines()
    for line in lines:
        line = line.replace('\n', '')
        corewords.append(str(line))
    return corewords

def similartocorews(model,word):
    corewords = coreword()
    sum = 0
    for word1 in corewords:
        sum = sum + model.similarity(word1,word)
    return sum/len(corewords)

def rank(model,wordset):#按照和证据类的词的相似度进行排序
    wordsimilar = {}
    for word in wordset:
        try:
            wordsimilar[word] = similartocorews(model,word)
        except KeyError:
            continue
    wordsimilar = sorted(wordsimilar.items(), key=lambda x: x[1], reverse=True)
    wordset1 = []
    for item in wordsimilar:
        wordset1.append(item[0])
    return wordset1

def closewordset(model,wordset):#计算一个词集内部的紧密程度
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

if __name__ == "__main__":
    event = '红黄蓝'
    model = Word2Vec.load("E:\SIGIR\Embedding/word_embedding")
    wordset = getwords(event,model)
    wordset = rank(model,wordset)
    #print(wordset)
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
        #print(word+' '+str(close))
        resultlist3[word] = close
    for i in range(0,len(wordset)-1):
        if resultlist3[wordset[i]] > resultlist3[wordset[i+1]]:
            resultlist4.append(wordset[i])
        else:
            break

    f = open('E:\SIGIR\证据类种子词库\红黄蓝\红黄蓝长新闻种子词库.txt','w')
    for word in resultlist4:
        f.write(word+'\n')
    f.close()

