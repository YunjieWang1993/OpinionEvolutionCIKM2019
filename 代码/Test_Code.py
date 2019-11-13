# import os
# from openpyxl import load_workbook
#
# workbook = load_workbook('D:\success\data\weibo_data.xlsx')
# sheet = workbook['weibo_data']
# sort_news = {}
# sort_time = {}
# for num in range(2,sheet.max_row):
#     repost = int(sheet.cell(row=num, column=6).value)
#     comment = int(sheet.cell(row=num, column=7).value)
#     praise = int(sheet.cell(row=num, column=8).value)
#     sum = repost+comment+praise
#     line = str(sheet.cell(row=num, column=3).value)
#     time = str(sheet.cell(row=num, column=13).value)
#     sort_news[line] = sum
#     sort_time[time] = sum
# sort_news = sorted(sort_news.items(),key = lambda x:x[1],reverse = True)
# sort_time = sorted(sort_time.items(),key = lambda x:x[1],reverse = True)
# f1 = open('C:/Users\hj\Desktop/news_jg.txt','w',encoding='utf-8',errors='ignore')
# f2 = open('C:/Users\hj\Desktop/times_jg.txt','w',encoding='utf-8',errors='ignore')
# for key in sort_news:
#     f1.write(str(key)+'\n')
# for key in sort_time:
#     f2.write(str(key)+'\n')
# f1.close()
# f2.close()

# import os
# # from openpyxl import load_workbook
# # import re
# # import jieba
# #
# # jieba.add_word('杭州')
# # dir = 'E:\SIGIR\weiboData_hzbm.xlsx'
# # workbook = load_workbook(dir)
# # sheet = workbook['Sheet1']
# # for num in range(2,sheet.max_row):
# #     time = sheet.cell(row=num, column=4).value
# #     time_day = int(time[0:4]+time[5:7]+time[8:10])
# #     time_hour = int(time[11:13])
# #     #print(time_day)
# #     if time_day == 20170702:
# #         print(time_day)
# #         line = sheet.cell(row=num, column=5).value.replace(' ', '')
# #         line = re.sub('[\s+\.\!\/_$%^*(+\"\')]+|[+——()?【】“”！。？、~@#￥%……&*（）]+', "", line)
# #         print(line)
# #         f = open('E:\SIGIR\延迟测试/20170702-'+str(time_hour)+'.txt','a',encoding='utf-8',errors='ignore')
# #         linelist = jieba.cut(line)
# #         if '杭州' in linelist:
# #             f.write(line + '\n')
# #         f.close()
#
# # import jieba
# # from openpyxl import load_workbook
# # import matplotlib.pyplot as plt
# # import math
# # import numpy as np
# # from pylab import *
# # sentiment_dict = {}
# # sentiment_words = []
# # # lines = open('D:\success\情感词典\BosonNLP_sentiment_score\BosonNLP_sentiment_score.txt','r',encoding='UTF-8').readlines()
# # # for line in lines:
# # #         word, score = line.split()
# # #         sentiment_dict[word] = float(score)
# # #         sentiment_words.append(word)
# # workbook = load_workbook('D:/success/ciku/大连理工大学情感词汇本体库.xlsx')
# # sheet = workbook['Sheet1']
# # for num in range(2, sheet.max_row):
# #     sentiment_dict[sheet.cell(row=num, column=1).value] = sheet.cell(row=num, column=6).value
# #     sentiment_words.append(sheet.cell(row=num, column=1).value)
# # line1111 = open('C:/Users\hj\Desktop/1111.txt').readline()
# # line1116 = open('C:/Users\hj\Desktop/1116.txt').readline()
# # word_list1111 = jieba.cut(line1111)
# # word_list1111 = [w for w in word_list1111]
# # word_list1116 = jieba.cut(line1116)
# # word_list1116 = [w for w in word_list1116]
# # sum1111 = 0
# # sum1116 = 0
# # count1111 = 0
# # count1116 = 0
# # for word in word_list1111:
# #     if word in sentiment_words:
# #         sum1111+=1
# #         count1111 = count1111 + sentiment_dict[word]
# # for word in word_list1116:
# #     if word in sentiment_words:
# #         sum1116+=1
# #         count1116 = count1116 + sentiment_dict[word]
# # print(count1111)
# # print(count1116)
# # importance1116 = 0.2937*(count1116/(count1116+count1111))
# # importance1111 = 0.2937*(count1111/(count1111+count1116))
# # x = np.arange(12.0, 14.0, 0.02)
# # y1111 = []
# # for i in x:
# #     y1111.append(2 * importance1111*math.pow(math.e, float(-2 * i)))
# # y1116 = []
# # for i in x:
# #     y1116.append(2 * importance1116*math.pow(math.e, float(-2 * i)))
# # xlim(0, 14)
# # plt.plot(x,y1111,color = 'red')
# # plt.plot(x,y1116,color = 'blue')
# # plt.ylabel('Event Importance')
# # plt.xlabel('Time Points')
# # plt.show()
# # # print(sum1111)
# # # print(sum1116)
# # # print(count1111/sum1111)
# # # print(count1116/sum1116)
# # # 还是不要取平均值了，就取总和，这样更准确一点。
#
# # from openpyxl import load_workbook#江歌案按照时间点分割新闻
# # import time
# # def datetime_toString(dt):#把datatime类型转变为str类型
# #     return dt.strftime("%Y-%m-%d-%H")
# # workbook = load_workbook('E:\SIGIR\weibo_data.xlsx')
# # sheet = workbook['weibo_data']
# # for num in range(2, sheet.max_row):
# #     time = sheet.cell(row=num, column=13).value
# #     time = datetime_toString(time)
# #     time = time[0:4] + time[5:7]
# #     f = open('E:\SIGIR\江歌案每月新闻/'+time+'.txt','a',encoding='utf-8', errors='ignore')
# #     f.write(str(sheet.cell(row=num, column=3).value)+'\n')
# #     f.close()
#
# # import jieba
# # import os
# # import re
# #
# # files = os.listdir('E:\SIGIR\事件时间线分析\江歌案每月新闻 - UTF-8')
# # stop_words = [w.strip() for w in open('D:/success/ciku/chinese_stopword.txt').readlines()]
# # sentiment_words = []
# # lines = open('D:\success\情感词典\BosonNLP_sentiment_score\BosonNLP_sentiment_score.txt','r',encoding='UTF-8').readlines()
# # for line in lines:
# #         word, score = line.split()
# #         sentiment_words.append(word)
# # jieba.add_word('江歌妈妈')
# # jieba.add_word('刘鑫')
# # for file in files:
# #     f = open('E:\SIGIR\事件时间线分析\江歌案每月新闻分词结果/'+file,'w',encoding='utf-8', errors='ignore')
# #     lines = open('E:\SIGIR\事件时间线分析\江歌案每月新闻 - UTF-8/' + file, 'r',encoding='utf-8', errors='ignore').readlines()
# #     word_list_F = []
# #     for line in lines:
# #         line = re.sub('[\s+\.\!\/_$%^*(+\"\')]+|[+——()?【】“”,！。？、~@#￥%……&*（）]+', "", line)
# #         word_list = jieba.cut(line)
# #         word_list = [w for w in word_list]
# #         for word in word_list:
# #             if len(word)>=2 and word not in stop_words and word not in sentiment_words and word not in word_list_F:
# #                 word_list_F.append(word)
# #     for word in word_list_F:
# #         f.write(word+'\n')
# #     f.close()
#
# import re
# # import os
# # #独特词不行
# # #LDA？
# #
# # files = os.listdir('E:\SIGIR\事件时间线分析\江歌案时间点新闻')
# # words = []
# # for file in files:
# #     line = open('E:\SIGIR\事件时间线分析\江歌案时间点新闻/'+file,'r',encoding='utf-8', errors='ignore').readline()
# #     word_list = line.strip().split(' ')
# #     for word in word_list:
# #         words.append(word)
# # print(words)
# # word_count={}
# # for word in words:
# #     sum=0
# #     for word2 in words:
# #         if word == word2:
# #             sum+=1
# #     word_count[word] = sum
# # for word in word_count:
# #     print(word_count[word])
# # for file in files:
# #     line = open('E:\SIGIR\事件时间线分析\江歌案时间点新闻/'+file,'r',encoding='utf-8', errors='ignore').readline()
# #     word_list = line.strip().split(' ')
# #     f = open('E:\SIGIR\事件时间线分析\江歌案每月新闻分词结果_保留独特词/'+file,'w',encoding='utf-8', errors='ignore')
# #     for word in word_list:
# #         if word_count[word] ==1:
# #             f.write(word+'\n')
# #     f.close()
#
# # import os
# # import re
# # files = os.listdir('E:\SIGIR\事件时间线分析\江歌案每月新闻 - UTF-8')
# # for file in files:
# #     lines  = open('E:\SIGIR\事件时间线分析\江歌案每月新闻 - UTF-8/'+file,'r',encoding='utf-8', errors='ignore').readlines()
# #     f = open('E:\SIGIR\事件时间线分析\江歌案每月新闻 - UTF-8/'+file,'w',encoding='utf-8', errors='ignore')
# #     for line in lines:
# #         line = re.sub('[\s+\.\!\/_$%^*(+\"\')a-zA-Z0-9]+|[+——()?【】“”！。？、~@#￥%……&*（）]+', "", line)
# #         print(line)
# #         f.write(line+'\n')
# #     f.close()
#
# # import os
# # files = os.listdir('E:\SIGIR\事件时间线分析\江歌案每月新闻分词结果')
# # word_list = {}
# # i = 0
# # for file in files:
# #     line = open('E:\SIGIR\事件时间线分析\江歌案每月新闻分词结果/'+file,'r',encoding='utf-8', errors='ignore').readline()
# #     word_list[i] = line.strip().split(' ')
# #     i+=1
# # word_list_D = {}
# # for i in range(1,15):
# #     word_list_D[i] = []
# #     for word in word_list[i]:
# #         if word not in word_list[i-1]:
# #             word_list_D[i].append(word)
# # word_list_D_qc = {}
# # for i in range(1,15):
# #     word_list_D_qc[i] = []
# #     for word in word_list_D[i]:
# #         if word not in word_list_D_qc[i]:
# #             word_list_D_qc[i].append(word)
# # f = open('E:\SIGIR\事件时间线分析\相邻时间点不同词结果.txt','w')
# # for i in range(1,15):
# #     f.write('时间点：'+str(i)+'\n')
# #     for word in word_list_D_qc[i]:
# #         f.write(word+' ')
# #     f.write('\n')
# # f.close()
#
# # word = '1.13'
# # print(word.isdigit())
#
# # import sentiment
# #
# # lines = open('E:\SIGIR\事件时间线分析\山东辱母案新闻\山东辱母案新闻.txt').readlines()
# # entity_list = []
# # sentiment_line = {}
# # for line in lines:
# #     print(line)
# #     print(abs(sentiment.judge_line(line,entity_list)))
#     #print(line)
#     #sentiment_line[line] = abs(sentiment.judge_line(line,entity_list))
# # sentiment_line = sorted(sentiment_line.items(),key = lambda x:x[1],reverse = True)
# # for line_score in sentiment_line:
# #     print(line_score[0]+'\n')
#
# # line1 = '卫计委回应榆林产妇坠亡事件：将依法依规严肃处理。'
# # line2 = '产妇母亲：我怎么可能让亲生女儿痛到寻死。'
# # entity_list = []
# # print(sentiment.judge_line(line1,entity_list))
# # print(sentiment.judge_line(line2,entity_list))
#
keywords = ['乐天']
lines = open('E:\SIGIR\事件数据\经济乐天\乐天.txt','r',encoding='utf-8', errors='ignore').readlines()
f = open('E:\SIGIR\事件数据\经济乐天\乐天.txt','w',encoding='utf-8', errors='ignore')
for line in lines:
    isline = False
    for keyword in keywords:
        if keyword in line:
            isline = True
            break
    if isline == True:
        f.write(line)
f.close()
#
#
# # list1 = ['wang','yun','jie']
# # list2 = []
# # for word in list1:
# #     list3 = []
# #     list2.append(word)
# #     for word1 in list1:
# #         if word1 not in list2:
# #             list3.append(word1)
# #     print(list2)
# #     print(list3)
# from gensim.models import Word2Vec
# model = Word2Vec.load("E:\SIGIR\Embedding/word_embedding")
# print(model.similarity('证据','胎儿'))
# print(model.similarity('证据','监控'))

# event = '魏则西'
# lines = open('E:\SIGIR\SVM\特征\反转/'+event+'/'+event+'.txt','r').readlines()
# lines2 = []
# for line in lines:
#     not_words = [w.strip() for w in open('D:/success/ciku/notDict.txt').readlines()]
#     for word in not_words:
#         if word in line:
#             line = line.replace(word,'')
#     lines2.append(line)
# f = open('E:\SIGIR\SVM\特征\反转/'+event+'/'+event+'去否定词.txt','w')
# for line in lines2:
#     f.write(line)
# f.close()

# dict = {}
# dict['wang'] = 1
# dict['yun'] = 2
# dict['jie'] = 3