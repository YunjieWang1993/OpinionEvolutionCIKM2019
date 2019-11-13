#  -*- coding: utf-8 -*-
import pandas as pd
import tweepy
import csv
import os
import re
consumer_key = '6bmBUsSJQ1ZVGCSJOBOnFGUzb'
consumer_secret = '6resZGye4HJlOzZOTHHQJsykw79JqUHKaqwJdpDYokghhvP6ZP'
access_token = '900699421456846849-eme1YzogPxQZgDbAuIvhOAL6MJyw17Z'
access_secret = 'hJ8Z4RvrZMKu70HdyER6Oajob9HinAlqalOWbHyWrlEb3'

def retrieve_tweets(input_file, output_file):
    """
    Takes an input filename/path of tweetIDs and outputs the full tweet data to a csv
    """

    # Authorization with Twitter

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5,
                     retry_errors=set([401, 404, 500, 503]), proxy="127.0.0.1:2055")

    # Read input file

    #df = pd.read_csv(input_file)
    twitterIDs  = open(input_file,'r').readlines()
    output = open(output_file, 'w',encoding='utf-8')


    #for tweetid in df.iloc[:, 0]:
    for tweetid in twitterIDs:
        p1 = re.compile(r'RT @.+?:')  ##转发标志
        p2 = re.compile(r'.?@\S+')  ##at某人
        p3 = re.compile(r'https?://[^/]+?/.+')  # 链接
        p4 = re.compile(r'#\S+')  ##话题标签
        try:
            status = api.get_status(tweetid)
            text = p4.sub('', p3.sub('', p2.sub('', p1.sub('', status.text.strip().replace('\n','')))))
            output.write(str(status.created_at)+' '+text+'\n')
        except Exception as e:
            print(e)
            pass
        # p1 = re.compile(r'RT @.+?:')  ##转发标志
        # p2 = re.compile(r'.?@\S+')  ##at某人
        # p3 = re.compile(r'https?://[^/]+?/.+')  # 链接
        # p4 = re.compile(r'#\S+')  ##话题标签
        # try:
        #     print('aaa')
        #     status = api.get_status(tweetid)
        #     print(status.text)
        #     print('bbb')
        #     if len(p4.sub('', p3.sub('', p2.sub('', p1.sub('', status.text.decode("utf-8").encode("gb2312").strip().replace('\n','')))))) < 10:
        #         print('111')
        #         continue
        #     else:
        #         print('222')
        #         lineInfos = "{\"id\": \"" + str(status.id) + "\"," + "\"date\": \"" + str(status.created_at) + "\"," + "\"text\" :\"" + status.text.decode("utf-8").encode("gb2312").strip().replace('\n',' ') + "\","
        #         lineInfos += "\"favourites_count\" :\"" + str(status.user.favourites_count) + "\"," + "\"statuses_count\" :\"" + str(status.user.statuses_count) + "\"," + "\"verified\" :\"" + str(status.user.verified)+"\","
        #         lineInfos +=   "\"following\" :\"" + str(status.user.following) + "\"," + "\"listed_count\" :\"" + str(status.user.listed_count) + "\"," + "\"followers_count\" :\"" + str(status.user.followers_count)+"\","
        #         lineInfos +=  "\"friends_count\" :\"" + str(status.user.friends_count)  + "\"," + "\"favorite_count\" :\"" +  str(status.favorite_count)  + "\"," + "\"retweeted\" :\"" +  str(status.retweeted)+"\","
        #         lineInfos +=  "\"retweet_coun\" :\"" + str(status.retweet_count) + "\"}"
        #         print(lineInfos)
        #         output.write(lineInfos + "\n")
        #
        # except Exception as e:
        #     print(e)
        #     pass

if __name__ == "__main__":
    input_file = 'E:\SIGIR\推特数据/twitterID.txt'
    output_file = 'E:\SIGIR\推特数据/twitterData.txt'
    retrieve_tweets(input_file,output_file)