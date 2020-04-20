# encoding='utf-8'
import random
import time

import requests
import urllib3
import threading

from spiders_helps.other_helper import ConfigHelp
from parse.parse_info import video_info_parse

urllib3.disable_warnings()
conf = ConfigHelp()

def get_cid(aid):
    url = "https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp".format(aid)
    payload = {}
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    cid = response.json()['data'][0]['cid']
    return cid


# def get_video_info(aid):
def get_video_info(q):
    if  not q.empty():
        aid = q.get()
        cid = get_cid(aid)
        # url = "https://api.bilibili.com/x/web-interface/view?aid=85054372&cid={}".format(cid)
        url = "https://api.bilibili.com/x/web-interface/view?cid={}&bvid={}".format(cid, aid)
        headers = conf['bilibili_conf']['headers']
        headers['Origin'] = 'https://www.bilibili.com'
        headers['Host'] = 'api.bilibili.com'
        response = requests.get(url, headers=headers, verify=False)
        time.sleep(random.choice([0.5,1]))
        title, desc, pubdata, tname, view, danmaku, coins, share, reply, like, favorite = video_info_parse(response)
        return title, desc, pubdata, tname, view, danmaku, coins, share, reply, like, favorite


if __name__ == '__main__':
    aid = '78976165'
    video_link = 'https://www.bilibili.com/video/av78976165'
    cookies = ''
    cid = get_cid(aid)
    get_video_info(aid)
