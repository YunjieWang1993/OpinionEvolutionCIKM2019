import math
import jieba
from openpyxl import load_workbook
import re


def count_min(i,j,sen_word,degree_word,not_words,degree_dict,word_list_2,a,sigma):
    sum_not=0
    sum_degree=0
    x = -math.pow(j-a,2)/(2*math.pow(sigma,2))
    for m in range(i+1,j):
        if word_list_2[m] in not_words:
            sum_not+=1
        elif word_list_2[m] in degree_dict:
            sum_degree=sum_degree+degree_word[m]
    if(sum_degree==0):
        return math.pow(-1,sum_not)*sen_word[j]*math.exp(x)
    else:
        return math.pow(-1,sum_not)*sum_degree*sen_word[j]*math.exp(x)
def count_min_1_1(a,j,sen_word,degree_word,not_words,degree_dict,word_list_2,sigma):
    sum_not=0
    sum_degree=0
    x = -math.pow(j-a,2)/(2*math.pow(sigma,2))
    for m in range(a+1,j):
        if word_list_2[m] in not_words:
            sum_not+=1
        elif word_list_2[m] in degree_dict:
            sum_degree=sum_degree+degree_word[m]
    if(sum_degree==0):
        return math.pow(-1,sum_not)*sen_word[j]*math.exp(x)
    else:
        return math.pow(-1,sum_not)*sum_degree*sen_word[j]*math.exp(x)
def count_min_1_2(j,a,sen_word,degree_word,not_words,degree_dict,word_list_2,sigma):
    sum_not=0
    sum_degree=0
    x = -math.pow(j-a,2)/(2*math.pow(sigma,2))
    for m in range(j+1,a):
        if word_list_2[m] in not_words:
            sum_not+=1
        elif word_list_2[m] in degree_dict:
            sum_degree=sum_degree+degree_word[m]
    if(sum_degree==0):
        return math.pow(-1,sum_not)*sen_word[j]*math.exp(x)
    else:
        return math.pow(-1,sum_not)*sum_degree*sen_word[j]*math.exp(x)
def judge_line(sentiment_dict,line):
    sigma = 21
    not_words = [w.strip() for w in open('D:/success/ciku/notDict.txt').readlines()]
    degree_words = open('D:/success/ciku/degreeDict.txt').readlines()
    degree_dict = {}
    for w in degree_words:
        word, score = w.strip().split(' ')
        degree_dict[word] = float(score)
    jieba.add_word('百度')
    for word in not_words:
        jieba.add_word(word)
    line = re.sub('[\s+\.\!\/_$%^*(+\"\')]+|[+——()?【】“”！。，？、~@#￥%……&*（）]+', "", line)
    word_list = jieba.cut(line)
    word_list = [w for w in word_list]
    #print(word_list)
    word_list_2 = []
    for word in word_list:
        if word in sentiment_dict:
            word_list_2.append(word)
        elif word in degree_dict:
            word_list_2.append(word)
        elif word in not_words:
            word_list_2.append(word)
        elif word == '百度':
            word_list_2.append(word)
    sen_word = {}
    not_word = {}
    degree_word = {}
    for index, word in enumerate(word_list_2):
        if word in sentiment_dict and word not in not_words and word not in degree_dict:
            sen_word[index] = sentiment_dict[word]
        elif word in not_words and word not in degree_dict:
            not_word[index] = -1
        elif word in degree_dict:
            degree_word[index] = degree_dict[word]
    if (len(sen_word) == 0):
        return 0
    sum_emotion = 0
    sen_loc = list(sen_word.keys())
    entities = []
    sum_entity = 0
    for a in range(0, len(word_list_2)):
        if (word_list_2[a] == '百度'):
            entities.append(a)
    for a in entities:
        #print(a)
        if (len(sen_loc) == 1):
            if a < sen_loc[0]:
                sum_emotion = count_min_1_1(a,sen_loc[0],sen_word,degree_word,not_words,degree_dict,word_list_2,sigma)
            if a > sen_loc[0]:
                sum_emotion = count_min_1_2(sen_loc[0],a,sen_word,degree_word,not_words,degree_dict,word_list_2,sigma)
        for i in range(0, len(sen_loc) - 1):
                sum_emotion = sum_emotion + count_min(sen_loc[i], sen_loc[i + 1], sen_word, degree_word, not_words, degree_dict,
                                              word_list_2, a, sigma)
        avg_emotion = sum_emotion / len(sen_loc)
        sum_entity = sum_entity + avg_emotion
    #print(entities)
    return sum_entity/len(entities)
def in_or_not_in_line(sentiment_words,line):
    not_words = [w.strip() for w in open('D:/success/ciku/notDict.txt').readlines()]
    jieba.add_word('百度')
    for word in not_words:
        jieba.add_word(word)
    word_list = jieba.cut(line)
    word_list = [w for w in word_list]
    for word in word_list:
        if word in sentiment_words:
            return 1
