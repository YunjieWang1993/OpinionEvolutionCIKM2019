import jieba

def Chusquare(eventlist):
    lines = []
    stop_words = [w.strip() for w in open('D:/success/ciku/chinese_stopword.txt').readlines()]
    for event in eventlist:
        lines = lines + open('E:\SIGIR\卡方检验/'+event+'.txt','r').readlines()
    sentimentindex = {}
    sentimentindex['产妇'] = [0,1,4,6,8,15,16]
    sentimentindex['红黄蓝'] = [4,9,12,13,14]
    sentimentindex['山东'] = [2,6,8]
    sentimentindex['魏则西'] = [8,9]
    sentimentlist = []
    for event in eventlist:
        lines1 = open('E:\SIGIR\卡方检验/' + event + '.txt', 'r').readlines()
        for i in sentimentindex[event]:
            sentimentlist.append(lines1[i])
    N = len(lines)
    wordset = []
    for line in lines:
        wordlist = jieba.cut(line)
        wordlist = [w for w in wordlist if w.replace('.','').isdigit() is False and len(w)>=2 and w not in stop_words]
        wordset = wordset + wordlist
    wordset2 = []
    for w in wordset:
        if w not in wordset2:
            wordset2.append(w)
    wordset = wordset2
    wordscore = {}
    for word in wordset:
        #print(word)
        a = 0
        b = 0
        c = 0
        d = 0
        for line in lines:
            if word in line and line in sentimentlist:
                a += 1
            if word in line and line not in sentimentlist:
                b += 1
            if word not in line and line in sentimentlist:
                c += 1
            if word not in line and line not in sentimentlist:
                d += 1
        wordscore[word] = (N*pow(a*d-c*b,2))/((a+c)*(b+d)*(a+b)*(c+d))
        # if word == '调查':
        #     print(a,b,c,d)
        #     print(wordscore[word])
    #print(wordscore)
    #sorted(wordscore)
    return wordscore
    # eventtestlist = []
    # for event in eventtotallist:
    #     if event not in eventlist:
    #         eventtestlist.append(event)
    # for event in eventtestlist:
    #     lines = open('E:\SIGIR\卡方检验/'+event+'.txt','r').readlines()
    #     resultindex = []
    #     i = 0
    #     for line in lines:
    #         sum = 0
    #         wordlist = jieba.cut(line)
    #         wordlist = [w for w in wordlist if w.replace('.', '').isdigit() is False and len(w) >= 2]
    #         wordlist2 = []
    #         for word in wordlist:
    #             if word not in wordlist2:
    #                 wordlist2.append(word)
    #         wordlist = wordlist2
    #         for word in wordlist:
    #             if word in wordset:
    #                 sum+=wordscore[word]
    #         if sum >= sigma:
    #             resultindex.append(i)
    #         i+=1
    #     sump = 0
    #     sumr = 0
    #     print(resultindex)
    #     for i in resultindex:
    #         if i in sentimentindex[event]:
    #             sump+=1
    #     p = sump/len(resultindex)
    #     for i in sentimentindex[event]:
    #         if i in resultindex:
    #             sumr+=1
    #     r = sumr/len(sentimentindex[event])
    #     print(event+' '+str(p)+' '+str(r))






if __name__ == "__main__":
    eventlist = ['红黄蓝','山东','魏则西']
    wordscore = Chusquare(eventlist)
    print(wordscore)
    print(wordscore['调查'])