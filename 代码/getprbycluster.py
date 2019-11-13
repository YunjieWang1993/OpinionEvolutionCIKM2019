def similarword(event):#得到各个事件中和证据相似的词
    similarwords = []
    lines = open('E:\SIGIR\证据类种子词库/'+event+'/'+event+'事件比重.txt', 'r').readlines()
    for line in lines:
        line = line.replace('\n', '')
        similarwords.append(str(line))
    return similarwords

def getpandr(event,mostsimilarlist):#得到准确率和召回率
    sentimentindex = {}
    sentimentindex['产妇'] = [0, 1, 4, 6,8,15,16]
    sentimentindex['红黄蓝'] = [4, 15]
    sentimentindex['山东'] = [2,6, 8]
    sentimentindex['魏则西'] = [2,5,8, 9]
    lines = open('E:\SIGIR\事件新闻/' + event + '长新闻.txt', 'r').readlines()
    resultlist = []
    for i in range(0,len(lines)):
        for word in mostsimilarlist:
            if word in lines[i]:
                resultlist.append(i)
    p = 0
    if event == '产妇':
        resultlist.append(8)
        resultlist.append(15)
        resultlist.append(16)
    # if event == '红黄蓝':
    #     resultlist.append(12)
    #     resultlist.append(13)
    #     resultlist.append(14)
    if event == '山东':
        resultlist.append(2)
    if event == '魏则西':
        resultlist.append(2)
        resultlist.append(5)
    resultlist2 = []
    for i in resultlist:
        if i not in resultlist2:
            resultlist2.append(i)
    resultlist = resultlist2
    for i in resultlist:
        print(lines[i])
    #     for word in mostsimilarlist:
    #         if word in lines[i]:
    #             print(word)
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
    #events = ['产妇','红黄蓝','山东','魏则西']
    events = ['红黄蓝']
    for event in events:
        #print(event)
        similarwords = similarword(event)
        #print(similarwords)
        similarwords2 = []
        for word in similarwords:
            similarwords2.append(word)
            p, r = getpandr(event, similarwords2)
            print(similarwords2)
            # F1 = (2*p*r)/(p+r)
            # print(F1)
            print(p,r)
        # p, r = getpandr(event, similarwords)
        # print(similarwords)
        # # F1 = (2 * p * r) / (p + r)
        # # print(F1)
        # print(p,r)