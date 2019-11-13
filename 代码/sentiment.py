import math
import jieba
import re
from openpyxl import load_workbook

def count_for_MultiSenWord(i,j,sen_word,degree_word,not_words,degree_dict,word_list_2,a,sigma):
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
def count_for_oneSenWord_1(a,j,sen_word,degree_word,not_words,degree_dict,word_list_2,sigma):
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
def count_for_oneSenWord_2(j,a,sen_word,degree_word,not_words,degree_dict,word_list_2,sigma):
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
def judge_line(judge_line,entity_list):
    sentiment_dict = {}
    sentiment_words = []
    lines = open('D:\success\情感词典\BosonNLP_sentiment_score\BosonNLP_sentiment_score.txt', 'r',
                 encoding='UTF-8').readlines()
    for line in lines:
        word, score = line.split()
        sentiment_dict[word] = float(score)
        sentiment_words.append(word)
    sigma = 21
    not_words = [w.strip() for w in open('D:/success/ciku/notDict.txt').readlines()]
    stop_words = [w.strip() for w in open('D:/success/ciku/chinese_stopword.txt').readlines()]
    degree_words = open('D:/success/ciku/degreeDict.txt').readlines()
    degree_dict = {}
    for w in degree_words:
        word, score = w.strip().split(' ')
        degree_dict[word] = float(score)
    for word in entity_list:
        jieba.add_word(word)
    for word in not_words:
        jieba.add_word(word)
    line = re.sub('[\s+\.\!\/_$%^*(+\"\')a-zA-Z0-9]+|[+——()?【】“”！，：。？、~@#￥%……&*（）]+', "", judge_line)
    #print(line)
    word_list = jieba.cut(line)
    word_list = [w for w in word_list if w not in stop_words and len(w) >= 2]
    word_list_2 = []
    for word in word_list:
        if word in sentiment_dict:
            word_list_2.append(word)
        elif word in degree_dict:
            word_list_2.append(word)
        elif word in not_words:
            word_list_2.append(word)
        elif word in entity_list:
            word_list_2.append(word)
    #print(word_list_2)
    not_word = {}
    degree_word = {}
    sen_word = {}
    #senti_value = []
    for index, word in enumerate(word_list_2):
        if word in sentiment_dict and word not in not_words and word not in degree_dict:
            if abs(sentiment_dict[word]) > 2.0 :
                print(word+' '+str(abs(sentiment_dict[word]))+'\n')
            sen_word[index] = abs(sentiment_dict[word])
            #senti_value.append(abs(sentiment_dict[word]))
        elif word in not_words and word not in degree_dict:
            not_word[index] = -1
        elif word in degree_dict:
            degree_word[index] = degree_dict[word]
    #print(max(senti_value))
    if (len(sen_word) == 0):
        return 0
    sen_loc = list(sen_word.keys())
    #print(sen_loc)
    entities = []
    sum_emotion = 0
    sum_entity = 0
    for a in range(0, len(word_list_2)):
        if (word_list_2[a] in entity_list):
            entities.append(a)
    #print(entities)
    if len(entities) == 0:
        #print('no entity')
        for i in range(0,len(sen_loc)):
            sum_emotion = sum_emotion + sen_word[sen_loc[i]]
            return sum_emotion/len(sen_loc)
    else:
        for a in entities:
            #print(sen_loc)
            if (len(sen_loc) == 1):
                if a < sen_loc[0]:
                    sum_emotion = sum_emotion+count_for_oneSenWord_1(a, sen_loc[0], sen_word, degree_word, not_words, degree_dict,
                                                word_list_2, sigma)
                if a > sen_loc[0]:
                    sum_emotion = sum_emotion+count_for_oneSenWord_2(sen_loc[0], a, sen_word, degree_word, not_words, degree_dict,
                                                word_list_2, sigma)
            else:
                for i in range(0, len(sen_loc) - 1):
                    sum_emotion = sum_emotion + count_for_MultiSenWord(sen_loc[i], sen_loc[i + 1], sen_word, degree_word, not_words,
                                                          degree_dict,
                                                          word_list_2, a, sigma)
            avg_emotion = sum_emotion / len(sen_loc)
            sum_entity = sum_entity + avg_emotion
        return sum_entity/len(entities)
