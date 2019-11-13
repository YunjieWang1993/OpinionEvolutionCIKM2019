import judge_sentiment
import os
import jieba

sentiment_dict = {}
sentiment_words = []
lines = open('D:\success\情感词典\BosonNLP_sentiment_score\BosonNLP_sentiment_score.txt','r',encoding='UTF-8').readlines()
for line in lines:
        word, score = line.split()
        sentiment_dict[word] = float(score)
        sentiment_words.append(word)
files = os.listdir('E:\SIGIR\事件数据\魏则西之死')
f = open('E:\SIGIR/01文件\魏则西事件.txt','w')
for file in files:
    #print(file)
    lines = open('E:\SIGIR\事件数据\魏则西之死/' + file, 'r').readlines()
    sum = 0
    for line in lines:
        jieba.add_word('百度')
        word_list = jieba.cut(line)
        word_list = [w for w in word_list]
        if '百度' in word_list:
            sum +=1
            score = judge_sentiment.judge_line(sentiment_dict,line)
            if score > 0:
                f.write(str(1))
            if score < 0:
                f.write(str(0))
    print(sum)
    f.write('\n')
f.close()