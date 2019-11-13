import os
import Levenshtein

def similar(line1,line2):
    return Levenshtein.ratio(line1, line2)
def judge_similar(line1,lineset):
    for line in lineset:
        if similar(line1,line) >= 0.7:
            return False
    return True

if __name__ == "__main__":
    rootdir = 'E:\SIGIR\事件时间线分析\江歌案每月新闻 - UTF-8'
    list = os.listdir(rootdir)
    for listname in list:
        s = []
        lines = open('E:\SIGIR\事件时间线分析\江歌案每月新闻 - UTF-8/'+listname, 'r',encoding='utf-8', errors='ignore').readlines()
        f = open('E:\SIGIR\事件时间线分析\江歌案每月新闻 - UTF-8/' + listname, 'w',encoding='utf-8', errors='ignore')
        for line in lines:
            if judge_similar(line,s) is True:
                s.append(line)
        for line in s:
            f.write(line)