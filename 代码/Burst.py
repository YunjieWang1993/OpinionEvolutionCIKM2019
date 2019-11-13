# import scipy.stats
# import os
# import numpy as np
#
# def getpx(rootdir):
#     list = os.listdir(rootdir)
#     x = []
#     for listname in list:
#         lines = open(rootdir + '/' + listname, 'r',encoding='utf-8').readlines()
#         x.append(len(lines))
#     return x
#
# def getpy(word,rootdir):
#     list = os.listdir(rootdir)
#     y = []
#     for listname in list:
#         lines = open(rootdir + '/' + listname, 'r',encoding='utf-8').readlines()
#         sum = 0
#         for line in lines:
#             if word in line:
#                 sum += 1
#         y.append(sum)
#     return y
#
# def similarword(event):#得到各个事件中和证据相似的词
#     similarwords = []
#     lines = open('E:\SIGIR\证据类种子词库/'+event+'/'+event+'.txt', 'r').readlines()
#     for line in lines:
#         line = line.replace('\n', '')
#         similarwords.append(str(line))
#     return similarwords
#
#
# if __name__ == "__main__":
#     rootdir = 'E:\SIGIR\事件数据含重复微博版本\红黄蓝幼儿园虐童案'
#     event = '红黄蓝'
#     x = getpx(rootdir)
#     #print(x)
#     similarwords = similarword(event)
#     KLscore = {}
#     for word in similarwords:
#         y = getpy(word,rootdir)
#         newx = []
#         newy = []
#         for i in range(len(x)):
#             if y[i]!=0:
#                 newx.append(x[i])
#                 newy.append(y[i])
#         KL = (scipy.stats.entropy(newx, newy)+scipy.stats.entropy(newy,newx))/2
#         print(word)
#         print(newy)
#         print(newx)
#         KLscore[word] = KL
#     KLscore = sorted(KLscore.items(), key=lambda x: x[1], reverse=False)
#     for item in KLscore:
#         print(item[0]+' '+str(item[1]))
    # linescore = {}
    # lines = open('E:\SIGIR\事件新闻\红黄蓝.txt','r').readlines()
    # for line in lines:
    #     sum = 0
    #     count = 0
    #     line = line.replace('\n','')
    #     for word in similarwords:
    #         if word in line:
    #             count+=1
    #             sum = sum + KLscore[word]
    #     if count != 0:
    #         linescore[line] = sum/count
    # linescore = sorted(linescore.items(), key=lambda x: x[1], reverse=False)
    # for item in linescore:
    #     print(item[0]+' '+str(item[1]))


# 词和爆发点之间的距离
import os
import jieba
import numpy as np

def similarword(event):#得到各个事件中和证据相似的词
    similarwords = []
    lines = open('E:\SIGIR\证据类种子词库/'+event+'/'+event+'.txt', 'r').readlines()
    for line in lines:
        line = line.replace('\n', '')
        similarwords.append(str(line))
    return similarwords

def allwords(event):
    lines = open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
    stop_words = [w.strip() for w in open('D:/success/ciku/chinese_stopword.txt').readlines()]
    words = []
    for line in lines:
        line = line.replace('\n','')
        wordlist = jieba.cut(line)
        wordlist = [w for w in wordlist if w.replace('.', '').isdigit() is False and len(w) >= 2 and w not in stop_words]
        for word in wordlist:
            if word not in words:
                words.append(word)
    return words

def getpx(event):
    rootdir = 'E:\SIGIR\事件数据含重复微博版本/'+ event
    lists = os.listdir(rootdir)
    x = []
    fre = []
    for listname in lists:
        lines = open(rootdir + '/' + listname, 'r',encoding='utf-8').readlines()
        x.append(lines)
        fre.append(len(lines))
    #print(fre)
    f = []
    for i in fre:
        f.append(i/sum(fre))
    return x,fre,f

def countword(word,x):
    c = []
    for i in x:
        count = 0
        for line in i:
            if word in line:
                count+=1
        c.append(count)
    # c1 = []
    # for i in c:
    #     c1.append(i/sum(c))
    return c

def outlier(x):
    o = []
    for i in range(len(x)):
        x1 = []
        for j in range(len(x)):
            if j != i:
                x1.append(x[j])
        a = np.mean(x1)
        b = np.std(x1, ddof=1)
        c = a + 2*b
        if x[i]>c:
            o.append(i)
    return o

def geto(event):
    o = {}
    o['山东'] = [1,12,35,62,90]
    o['红黄蓝'] = [5,6,8]
    o['魏则西'] = [2,3,4,5,10,11,12,13]
    o['产妇'] = [1,5]
    return o[event]

def getburstnews(event):
    x, fre, f = getpx(event)
    #words = similarword(event)
    words = allwords(event)
    score = {}
    #o = outlier(fre)
    #print(o)
    #o = [1,12,35,62,90]#山东案
    #o = [2,3,4,5,10,11,12,13]#魏则西
    #o = [5,6,8]#红黄蓝
    o = geto(event)
    for word in words:
        sumd = 0
        c = countword(word,x)
        # for i in range(len(c)):
        #     for j in range(len(f)):
        #         sumd = sumd + c[i]*f[j]*pow((i-j),2)
        for i in range(len(c)):
            for j in range(len(o)):
                #sumd = sumd + c[i]*pow((i-o[j]),2)
                sumd = sumd + c[i]*abs(i-o[j])
        if sum(c)!=0 :
            score[word] = sumd/sum(c)
    lines = open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
    words = score.keys()
    sums = 0
    linescore = {}
    for line in lines:
        line = line.replace('\n', '')
        count = 0
        sumg = 0
        mind = 100000
        for word in words:
            if word in line:
                sumg = sumg + score[word]

                count += 1
                if score[word] <= mind:
                    mind = score[word]
        if count != 0:
            linescore[line] = mind
            sums = sums + mind
    linescore1 = {}
    values = linescore.values()
    minn = min(values)
    maxn = max(values)
    distance = maxn - minn
    for line in lines:
        line = line.replace('\n','')
        linescore1[line] = ((linescore[line] - minn)/distance)*0.8+0.1
    return linescore1

if __name__ == "__main__":
    event = '魏则西'
    linescore = getburstnews(event)
    linescore = sorted(linescore.items(), key=lambda x: x[1], reverse=False)
    for item in linescore:
        print(item[0]+' '+str(item[1]))