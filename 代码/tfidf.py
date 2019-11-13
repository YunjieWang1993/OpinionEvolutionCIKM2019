# import jieba
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.feature_extraction.text import CountVectorizer
# def getcorpus(eventlist):
#     corpus = []
#     stop_words = [w.strip() for w in open('D:/success/ciku/chinese_stopword.txt').readlines()]
#     for event in eventlist:
#         lines = open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
#         for line in lines:
#             wordlist = jieba.cut(line)
#             wordlist = [w for w in wordlist if w.replace('.', '').isdigit() is False and len(w) >= 2 and w not in stop_words]
#             wordlist = str(wordlist)
#             corpus.append(wordlist)
#     return corpus
# if __name__ == "__main__":
#     eventlist = ['产妇']
#     corpus = getcorpus(eventlist)
#     #print(corpus)
#     vectorizer = CountVectorizer()
#     transformer = TfidfTransformer()
#     tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
#     weight = tfidf.toarray()
#     words  = vectorizer.get_feature_names()
#     print(len(weight))
#     for i in range(0,len(weight)):
#         print(sum(weight[i]))

import jieba
import math

def tf(word,line):
    stop_words = [w.strip() for w in open('D:/success/ciku/chinese_stopword.txt').readlines()]
    wordlist = jieba.cut(line)
    wordlist = [w for w in wordlist if w.replace('.', '').isdigit() is False and len(w) >= 2 and w not in stop_words]
    #print(wordlist)
    s = len(wordlist)
    c = wordlist.count(word)
    return c/s

def idf(word,lines):
    c = 0
    for line in lines:
        if word in line:
            c+=1
    s = len(lines)
    return math.log10(s/c)

def similarword(event):#得到各个事件中和证据相似的词
    similarwords = []
    lines = open('E:\SIGIR\证据类种子词库/'+event+'/'+event+'.txt', 'r').readlines()
    for line in lines:
        line = line.replace('\n', '')
        similarwords.append(str(line))
    return similarwords

def tfidf(event):
    lines = open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
    words = similarword(event)
    tfdir = {}
    idfdir = {}
    tfidfdir = {}
    for line in lines:
        line = line.replace('\n', '')
        tfscore = 0
        for word in words:
            if word in line:
                tfscore = tfscore + tf(word, line)
        tfdir[line] = tfscore
        idfscore = 0
        for word in words:
            if word in line:
                idfscore = idfscore + idf(word, lines)
        idfdir[line] = idfscore
        tfidfdir[line] = tfscore * idfscore
    return tfidfdir


if __name__ == "__main__":
    events = ['产妇']
    for event in events:
        tfidfdir = tfidf(event)
        tfidfdir = sorted(tfidfdir.items(), key=lambda x: x[1], reverse=True)
        for item in tfidfdir:
            print(item[0]+' '+str(item[1]))
