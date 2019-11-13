from gensim.models import Word2Vec

def coreword():#得到种子词库中的词
    corewords = []
    lines = open('E:\SIGIR\证据类种子词库\红黄蓝\红黄蓝长新闻种子词库.txt', 'r').readlines()
    for line in lines:
        line = line.replace('\n', '')
        corewords.append(str(line))
    return corewords

def filter(wordset,model):
    sum = 0
    for word in wordset:
        sum = sum + model.similarity(word,'证据')
    avg = sum/len(wordset)
    resultlist = []
    for word in wordset:
        if model.similarity(word,'证据') > avg:
            resultlist.append(word)
    return resultlist


if __name__ == "__main__":
    corewords = coreword()
    model = Word2Vec.load("E:\SIGIR\Embedding/word_embedding")
    resultlist = filter(corewords,model)
    f = open('E:\SIGIR\证据类种子词库\红黄蓝\红黄蓝长新闻种子词库筛选.txt', 'w')
    for word in resultlist:
        f.write(word+'\n')
    f.close()