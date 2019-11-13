import features
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from gensim.models import Word2Vec
import jieba
import Burst


def svm(theevent):
    totalevents = ['产妇', '红黄蓝', '山东', '魏则西']
    eventlist = []
    for e in totalevents:
        if e != theevent:
            eventlist.append(e)
    #print(eventlist)
    lines = []
    stop_words = [w.strip() for w in open('D:/success/ciku/chinese_stopword.txt').readlines()]
    for event in eventlist:
        lines1 = open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
        for line in lines1:
            line = line.replace('\n', '')
            lines.append(line)
    sentimentindex = {}
    sentimentindex['产妇'] = [0, 1, 4, 6, 8, 15, 16]
    sentimentindex['红黄蓝'] = [4, 9, 13, 14]
    sentimentindex['山东'] = [2, 6, 8]
    sentimentindex['魏则西'] = [2, 5, 8, 9]
    shiftlist = []  # 引起shift的news的集合
    for event in eventlist:
        lines1 = open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
        for i in sentimentindex[event]:
            line = lines1[i].replace('\n', '')
            shiftlist.append(line)
    totalsenevent = ['产妇','红黄蓝','山东']#含有情感最大的event
    totalrevevent = ['产妇', '红黄蓝', '魏则西']#含有反转的event
    seneventlist = []
    reveventlist = []
    for e in eventlist:
        if e in totalsenevent:
            seneventlist.append(e)
        if e in totalrevevent:
            reveventlist.append(e)
    sentimentlines = []
    reverselines = []
    for e in seneventlist:
        sentimentlines.append(features.findmaxsentiment(e))
    for e in reveventlist:
        reverseline = features.findreverse(e)
        for line in reverseline:
            reverselines.append(line)
    #linescores,wordscore = features.Chusquare(totalevents)
    tfidfscores = {}
    for event in totalevents:
        tfidfdir = features.tfidf(event)
        for item in tfidfdir.items():
            tfidfscores[item[0]] = item[1]
    burstscore = {}
    for event in totalevents:
        burstevent = Burst.getburstnews(event)
        for item in burstevent.items():
            burstscore[item[0]] = item[1]
    x = []
    y = []
    for line in lines:
        arrayx = []
        # if line in sentimentlines:
        #     arrayx.append(1)
        # else:
        #     arrayx.append(0)
        # if line in reverselines:
        #     arrayx.append(1)
        # else:
        #     arrayx.append(0)
        #arrayx.append(linescores[line])
        arrayx.append(tfidfscores[line])
        arrayx.append(burstscore[line])
        x.append(arrayx)
        if line in shiftlist:
            y.append(1)
        else:
            y.append(0)
    clf = SVC()
    clf.fit(x,y)
    print(clf.score(x,y))
    prex = getx(theevent)
    prey = clf.predict(prex)
    #print(prey)
    resultlist = []
    for i in range(0,len(prey)):
        if prey[i] == 1:
            resultlist.append(i)
    #print(resultlist)
    p = 0
    for i in resultlist:
        if i in sentimentindex[theevent]:
            p+=1
    precision = p/len(resultlist)
    r = 0
    for i in sentimentindex[theevent]:
        if i in resultlist:
            r+=1
    recall = r/len(sentimentindex[theevent])
    return precision,recall

def getx(event):
    x = []
    totalevents = ['产妇', '红黄蓝', '山东', '魏则西']
    linescores, wordscore = features.Chusquare(totalevents)
    totalsenevent = ['产妇', '红黄蓝', '山东']
    totalrevevent = ['产妇', '红黄蓝', '魏则西']
    sentimentlines = []
    reverselines = []
    if event not in totalsenevent:
        sentimentlines = []
    else:
        sentimentlines.append(features.findmaxsentiment(event))
    if event not in totalrevevent:
        reverselines = []
    else:
        reverseline = features.findreverse(event)
        for line in reverseline:
            reverselines.append(line)
    lines = open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
    tfidfscore = features.tfidf(event)
    burstscore = Burst.getburstnews(event)
    for line in lines:
        #print(line)
        line = line.replace('\n','')
        arrayx = []
        # if line in sentimentlines:
        #     arrayx.append(1)
        # else:
        #     arrayx.append(0)
        # if line in reverselines:
        #     arrayx.append(1)
        # else:
        #     arrayx.append(0)
        arrayx.append(tfidfscore[line])
        arrayx.append(burstscore[line])
        #arrayx.append(linescores[line])
        x.append(arrayx)
    return x


if __name__ == "__main__":
    events = ['产妇', '红黄蓝', '山东','魏则西']
    for event in events:
        print(event)
        print(svm(event))
        print('--------')