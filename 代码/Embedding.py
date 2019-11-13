# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
import jieba
from numpy import *

def similar(model,wordset1,wordset2):
    sum = 0
    for word1 in wordset1:
        for word2 in wordset2:
            try:
                sum += model.similarity(word1,word2)
            except KeyError:
                #print('not in vocabulary')
                sum += 0
    return sum/(len(wordset1)*len(wordset2))

def word_set(eventlist):
    lines = []
    for event in eventlist:
        lines = lines + open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
    wordset = []
    for line in lines:
        wordlist = jieba.cut(line)
        wordlist = [w for w in wordlist if w.replace('.', '').isdigit() is False and len(w) >= 2]
        wordset = wordset + wordlist
    wordset2 = []
    for w in wordset:
        if w not in wordset2:
            wordset2.append(w)
    wordsets = []
    for word in wordset2:
        word = [word]
        wordsets.append(word)
    return wordsets

def maxtwo(wordsets,model):
    max = 0
    wordset1 = []
    wordset2 = []
    for i in range(0,len(wordsets)):
        for j in range(i+1,len(wordsets)):
            score = similar(model,wordsets[i],wordsets[j])
            if score >= max:
                max = score
                wordset1 = wordsets[i]
                wordset2 = wordsets[j]
    if max >= 0.3:
        # print('wordset1:')
        # print(wordset1)
        # print('wordset2:')
        # print(wordset2)
        # print(max)
        wordsetmerge = wordset1 + wordset2
        wordsets.remove(wordset1)
        wordsets.remove(wordset2)
        wordsets.append(wordsetmerge)
        return True
    else:
        return False
def pandr(eventlist):
    lines = []
    words = ['递交', '申请', '确认', '公布', '经查', '调查组', '调查', '调查结果', '高度重视', '审查', '整改']#魏则西
    #words = ['证明', '认定', '曝光', '公布', '通报', '调查', '调查结果']#山东
    #words = ['报案', '警方', '排查', '调查', '通报', '立案', '涉嫌', '涉案人员', '北京警方', '刑事拘留', '刑拘', '事件', '疑似', '涉事']#红黄蓝
    #words = ['监控', '调查', '通报', '施救', '依法', '依规', '停职', '严肃处理', '警方', '院方', '家属', '赔偿', '出示', '涉事']#产妇
    #words = ['发现', '认定', '确认', '结论', '证明', '监控', '排查', '整改', '审查', '通报', '调查', '调查结果', '曝光', '公布', '发布']
    for event in eventlist:
        lines = lines + open('E:\SIGIR\事件新闻/' + event + '.txt', 'r').readlines()
    sentimentindex = {}
    sentimentindex['产妇'] = [0, 1, 4, 6]
    sentimentindex['红黄蓝'] = [4, 9]
    sentimentindex['山东'] = [6, 8]
    sentimentindex['魏则西'] = [8, 9]
    resultindex = []
    i = 0
    for line in lines:
        wordlist = jieba.cut(line)
        wordlist = [w for w in wordlist if w.replace('.', '').isdigit() is False and len(w) >= 2]
        wordlist2 = []
        for word in wordlist:
            if word not in wordlist2:
                wordlist2.append(word)
        wordlist = wordlist2
        for word in words:
            if word in wordlist:
                resultindex.append(i)
        i+=1
    sump = 0
    sumr = 0
    for i in resultindex:
        if i in sentimentindex[event]:
            sump += 1
    p = sump / len(resultindex)
    for i in sentimentindex[event]:
        if i in resultindex:
            sumr += 1
    r = sumr / len(sentimentindex[event])
    return p,r





if __name__ == "__main__":
    # eventlist = ['魏则西']
    # model = Word2Vec.load("E:\SIGIR\Embedding/word_embedding")
    # #eventlist = ['产妇', '红黄蓝', '山东', '魏则西']
    # wordsets = word_set(eventlist)
    # while True:
    #     if maxtwo(wordsets,model) == False:
    #         break
    #     else:
    #         continue
    # for wordset in wordsets:
    #     print(wordset)

    eventlists = [['魏则西']]
    for eventlist in eventlists:
        p,r = pandr(eventlist)
        print(eventlist[0])
        print(p,r)
