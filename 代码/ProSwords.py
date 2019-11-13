# 对得到的相似词进行处理，来提高准确率
from gensim.models import Word2Vec

def similarword(event):#得到各个事件中和证据相似的词
    similarwords = []
    lines = open('E:\SIGIR\证据类种子词库/'+event+'.txt', 'r').readlines()
    for line in lines:
        line = line.replace('\n', '')
        similarwords.append(str(line))
    return similarwords

# 首先还是要去掉噪声词，然后再考虑结合时间和事件的爆发点

def rankbysim(similarwords):
    model = Word2Vec.load("E:\SIGIR\Embedding/word_embedding")
    simscore = {}
    for word in similarwords:
        sum = 0
        for word1 in similarwords:
            sum = sum + model.similarity(word,word1)
        simscore[word] = sum/len(similarwords)
    simscore = sorted(simscore.items(), key=lambda x: x[1], reverse=True)
    return simscore

if __name__ == "__main__":
    event = '产妇'
    similarwords = similarword(event)
    print(rankbysim(similarwords))