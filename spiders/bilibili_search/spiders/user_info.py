"""
用户信息
"""
import time
import requests
import urllib3

from spiders_helps.other_helper import ConfigHelp
from parse.parse_info import  user_info_parse1,user_info_parse2

urllib3.disable_warnings()
conf = ConfigHelp()
headers = conf['bilibili_conf']['headers']


# 账号昵称，账号id,账号主页，账号性别(保密，男，女)，账号简介,账号认证
def get_user_info1(mid):
    url = "https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp".format(mid)

    headers['Host'] = 'api.bilibili.com'
    headers['Origin'] = 'https://space.bilibili.com'
    headers['Referer'] = 'https://space.bilibili.com/{}'.format(mid)
    try:
        response1 = requests.request("GET", url, headers=headers,verify=False,timeout=60)
    except TimeoutError as e:
        count = 1
        while True:
            print('网络连接超时，重新获取{}次'.format(count))
            count+=1
            time.sleep(3)
            response1 = requests.request("GET", url, headers=headers, timeout=60, verify=False)
            if response1.status_code ==200:
                break
            if count==5:
                return 'null','null','null','null'

    name,mid,sex,sign = user_info_parse1(response1)
    return name, mid, sex, sign

#关注数，粉丝数，获赞数，播放数，阅读数
def get_user_info2(mid):
    url1 = "https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp&callback=__jp4".format(mid)
    url2 = "https://api.bilibili.com/x/space/upstat?mid={}&jsonp=jsonp&callback=__jp5".format(mid)
    headers['Host'] = 'api.bilibili.com'
    headers['Origin'] = 'https://space.bilibili.com'
    headers['Referer'] = 'https://space.bilibili.com/{}'.format(mid)
    try:
        response2_1 = requests.request("GET", url1, headers=headers,verify=False,timeout=60)
    except:
        count = 1
        while True:
            print('网络连接超时，重新获取{}次'.format(count))
            count+=1
            time.sleep(3)
            response2_1 = requests.request("GET", url1, headers=headers, timeout=60, verify=False)
            if response2_1.status_code ==200:
                break
            if count==5:
                return 'null'

    try:
        time.sleep(1)
        response2_2 = requests.request("GET", url2, headers=headers, verify=False, timeout=60)
    except:
        count = 1
        while True:
            print('网络连接超时，重新获取{}次'.format(count))
            count += 1
            time.sleep(3)
            response2_2 = requests.request("GET", url2, headers=headers, timeout=60, verify=False)
            if response2_2.status_code == 200:
                break
            if count == 5:
                return 'null'

    follower = user_info_parse2(response2_1,response2_2)
    return follower


# if __name__ == '__main__':
#     mid = '1542136'
#     # mid = '8047632'
#     cookies= ''
#     get_user_info1(mid)
#     get_user_info2(mid)

