import jieba
import os
import numpy as np

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

def similarword(event):#得到各个事件中和证据相似的词
    similarwords = []
    lines = open('E:\SIGIR\证据类种子词库/'+event+'/'+event+'.txt', 'r').readlines()
    for line in lines:
        line = line.replace('\n', '')
        similarwords.append(str(line))
    return similarwords

def getfre(event):
    rootdir = 'E:\SIGIR\事件数据含重复微博版本/'+ event
    lists = os.listdir(rootdir)
    x = []
    fre = []
    for listname in lists:
        lines = open(rootdir + '/' + listname, 'r',encoding='utf-8').readlines()
        x.append(lines)
        fre.append(len(lines))
    return x,fre

def outlier(x):
    o = []
    for i in range(len(x)):
        x1 = []
        for j in range(len(x)):
            if j != i:
                x1.append(x[j])
        a = np.mean(x1)
        b = np.std(x1, ddof=1)
        c = a + 3*b
        if x[i]>c:
            o.append(i)
    return o

def countword(word,x):
    c1 = []
    for i in x:
        count = 0
        for line in i:
            if word in line:
                count+=1
        c1.append(count)
    c = []
    for i in c1:
        c.append(i/sum(c1))
    return c,c1

# def getburstnews(event):
#     x, fre = getfre(event)
#     words = allwords(event)
#     #words = similarword(event)
#     o1 = outlier(fre)
#     resultwords = []
#     if o1 != []:
#         #print(o1)
#         for word in words:
#             c = countword(word, x)
#             o = outlier(c)
#             result = True
#             if o!=[]:
#                 for i in range(len(o)):
#                     if o[i] not in o1:
#                         result = False
#                 if result == True:
#                     #print(word, o, c[o[0]] / fre[o[0]])
#                     resultwords.append(word)
#     if o1 == []:
#         for word in words:
#             c = countword(word, x)
#             o = outlier(c)
#             if o != []:
#                 if c[o[0]]/fre[o[0]]>0.3:
#                     print(word, c[o[0]]/fre[o[0]],sum(c)/sum(fre),o)
#                     resultwords.append(word)
#     lines = open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
#     resultlines = []
#     for line in lines:
#         line = line.replace('\n', '')
#         for word in resultwords:
#             if word in line and line not in resultlines:
#                 resultlines.append(line)
#     return resultlines

def newsindex(event):
    indexs = {}
    indexs['产妇'] = [0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,3,3,5,5]
    indexs['红黄蓝'] = [0,0,0,0,0,0,0,1,1,1,1,1,2,2,3,3]
    return indexs[event]
def getburstnews(event):
    x, fre = getfre(event)
    print(fre)
    lines = open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
    indexs  = newsindex(event)
    i = 0
    resultlines = []
    for line in lines:
        print(line)
        ind = indexs[i]
        line = line.replace('\n', '')
        wordlist = jieba.cut(line)
        stop_words = [w.strip() for w in open('D:/success/ciku/chinese_stopword.txt').readlines()]
        wordlist = [w for w in wordlist if w.replace('.', '').isdigit() is False and len(w) >= 2 and w not in stop_words]
        for word in wordlist:
            c,c1 = countword(word,x)
            o = outlier(c)
            if len(o)==1 and o[0] == ind and c1[o[0]]/fre[o[0]]>0.3 and c1[o[0]]/fre[o[0]]<0.4:
                #print(word,c[o[0]]/fre[o[0]],sum(c)/sum(fre))
                print(word,c1[o[0]]/fre[o[0]])
                if line not in resultlines:
                    resultlines.append(line)
        i+=1
    return resultlines






if __name__ == "__main__":
    event = '产妇'
    resultlines = getburstnews(event)
    for line in resultlines:
        print(line)
    # x = [0.6065573770491803, 0.25, 0.40540540540540543, 0.45918367346938777, 0.35555555555555557, 0.375]
    # print(np.mean(x))
    # print(np.std(x,ddof=1))