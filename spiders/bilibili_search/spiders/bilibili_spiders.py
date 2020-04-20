import re
import time

import queue

import requests
import urllib3
from lxml import etree

from data.save_data import save
from spiders.video_info import get_video_info
from spiders.user_info import get_user_info1,get_user_info2
from spiders_helps.other_helper import ConfigHelp

urllib3.disable_warnings()
conf = ConfigHelp()
spider_name = 'bilibili'
q = queue.Queue()

def get_crawl_link(gjc,page):
    print("第{}页开始抓取".format(page))
    url = "https://search.bilibili.com/video?keyword={}&page={}".format(gjc,page)
    # url = "https://search.bilibili.com/all?keyword={}&page={}".format(gjc,page)
    headers =conf['bilibili_conf']['headers']
    headers['Host']='search.bilibili.com'
    response = requests.request("GET", url, headers=headers,timeout=60,verify=False)
    time.sleep(1)
    return response

def parse(response,gjc,save_time):
    pingtai = 'b站'
    tree = etree.HTML(response.text)
    li = tree.xpath('//ul[@class="video-list clearfix"]/li')

    for i in range(1,len(li)+1):
        print("第{}次抓取".format(i))
        total_info = []
        info = []
        time.sleep(1)
        video_link = 'https:'+tree.xpath('//ul[@class="video-list clearfix"]/li[{}]/a/@href'.format(i))[0]
        user_info_link = tree.xpath('//ul[@class="video-list clearfix"]/li[{}]/div[@class="info"]/div[@class="tags"]/span[@title="up主"]/a/@href'.format(i))[0]
        user_link = 'https:'+user_info_link
        mid = re.search(r'//space.bilibili.com/(\d+)', user_info_link).group(1)
        name,mid,sex,sign = get_user_info1(mid)
        follower = get_user_info2(mid)
        aid = re.search(r'https://www.bilibili.com/video/(.*?)\?from=search',video_link).group(1)
        title,desc,pubdata,tname,view,danmaku,coins,share,reply,like,favorite = get_video_info(aid)
        # info.append(pingtai)
        # info.append(gjc)
        # info.append(name)
        # info.append(mid)
        # info.append(user_link)
        # info.append(sex)
        # info.append(sign)
        # info.append(follower)
        # info.append(title)
        # info.append(video_link)
        # info.append(desc)
        # info.append(pubdata)
        # info.append(tname)
        # info.append(view)
        # info.append(danmaku)
        # info.append(coins)
        # info.append(share)
        # info.append(reply)
        # info.append(like)
        # info.append(favorite)
        otherStyleTime = time.strftime("%Y/%m/%d %H:%M",  time.localtime(int(time.time())))
        info.append(otherStyleTime)
        total_info.append(info)

        save(spider_name, save_time, total_info)
    return len(li)

if __name__ == '__main__':
    #关键词搜索
    save_time = time.strftime("%Y%m%d", time.localtime(int(time.time())))
    with open('../data/source.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            gjc = line.strip('\n')
            for page in range(1, 51):
                response = get_crawl_link(gjc, page)
                i = parse(response,gjc,save_time)
                #页数判断
                if i < 20:
                    print('没有页数啦，该{}页共有视频{}个'.format(page, i))
                    print(page)
                    break
