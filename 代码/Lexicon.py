import jieba
import re

word_frequency = {}
lines = open('E:\SIGIR\事件时间线分析\红黄蓝事件新闻\红黄蓝事件新闻简化版.txt','r')
stop_words = [w.strip() for w in open('D:/success/ciku/chinese_stopword.txt').readlines()]
not_words = [w.strip() for w in open('D:/success/ciku/notDict.txt').readlines()]
word_list_total = []
word_list_alone = []
for line in lines:
    #line = re.sub('[\s+\.\!\/_$%^*(+\"\')a-zA-Z0-9]+|[+——()?【】“”！。？、~@#￥%……&*（）]+', "", line)
    word_list = jieba.cut(line)
    word_list = [w for w in word_list if w.replace('.','').isdigit() is False]
    word_list = [w for w in word_list if len(w)>=2 or w in not_words]
    for word in word_list:
        if word not in word_list_alone:
            word_list_alone.append(word)
    word_list_total.append(word_list)
#print(word_list_total)
for word in word_list_alone:
    sum = 0
    for i in range(0,len(word_list_total)):
        if word in word_list_total[i]:
            sum+=1
    word_frequency[word] = sum/len(word_list_total)
#print(word_frequency['未'])
print(word_frequency['红黄蓝'])
f = open('E:\SIGIR\事件时间线分析\词库变化\红黄蓝事件词库变化.txt','w')
for i in range(0,len(word_list_total)):
    word_list_A = []
    for word in word_list_total[i]:
        if word_frequency[word]<=0.3 and word not in word_list_A:
            word_list_A.append(word)
    for word in word_list_A:
        f.write(word+' ')
    f.write('\n')
    f.write('\n')
# for i in range(1,len(word_list_total)):
#     f.write('时间点：'+str(i)+'\n')
#     word_list_A = []
#     word_list_B = []
#     for word in word_list_total[i]:
#         if word in word_list_total[i-1] and word_frequency[word]<=0.2 and word not in word_list_A:
#             word_list_A.append(word)
#     for word in word_list_A:
#         f.write(word+' ')
#     f.write('\n')
#     for word in word_list_total[i]:
#         if word not in word_list_total[i-1] and word_frequency[word]<=0.2 and word not in word_list_B:
#             word_list_B.append(word)
#     for word in word_list_B:
#         f.write(word+' ')
#     f.write('\n')

# for i in range(0,len(word_list_total)):
#     f.write('时间点：' + str(i) + '\n')
#     word_list_W = []
#     for word in word_list_total[i]:
#         if word_frequency[word] == 1 and word not in word_list_W:
#             word_list_W.append(word)
#     for word in word_list_W:
#         f.write(word+' ')
#     f.write('\n')
f.close()