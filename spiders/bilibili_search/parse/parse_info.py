#解析数据
import json
import re


def user_info_parse1(response1):
    user_info_json = response1.json()

    name = user_info_json['data']['name']
    mid = user_info_json['data']['mid']
    sex = user_info_json['data']['sex']
    sign = user_info_json['data']['sign'].replace('\r','').replace('\n','').replace('\t','')
    official_title = user_info_json['data']['official']['title']
    official_type = user_info_json['data']['official']['type']
    if official_title == "":
        official_title = "null"
    else:
        if official_type == 0:
            official_title = "bilibili个人认证：" + official_title
        elif official_type == 1:
            official_title = 'bilibili机构认证：' + official_title

    return name,mid,sex,sign


def user_info_parse2(response2_1,response2_2):
    user_info2_1_json = json.loads(re.match(".*?({.*}).*", response2_1.text, re.S).group(1))
    user_info2_2_json = json.loads(re.match(".*?({.*}).*", response2_2.text, re.S).group(1))

    # 关注数
    following = user_info2_1_json['data']['following']
    # 粉丝数
    follower = user_info2_1_json['data']['follower']
    # 获赞数
    likes = user_info2_2_json['data']['likes']
    # 播放数
    plays = user_info2_2_json['data']['archive']['view']
    # 阅读数
    reads = user_info2_2_json['data']['article']['view']
    if reads == 0:
        reads = 'None'
    return follower


def video_info_parse(response):
    # res_json = json.loads(response.text)
    res_json = response.json()
    # 标题
    title = res_json['data']['title']
    # 视频简介
    desc = res_json['data']['desc'].replace('\r', '').replace('\n', '').replace('\t', '')
    # 发布时间
    pubdata = res_json['data']['pubdate']
    # timeArray = time.localtime(pubdata)
    # pubdata = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # 视频所属类别
    tname = res_json['data']['tname']
    # 视频弹幕量
    danmaku = res_json['data']['stat']['danmaku']
    # 投币
    coins = res_json['data']['stat']['coin']
    # #阅读数
    # read = 'None'
    # 视频播放量
    view = res_json['data']['stat']['view']
    # 视频转发量
    share = res_json['data']['stat']['share']
    # 视频评论量
    reply = res_json['data']['stat']['reply']
    # 视频点赞数
    like = res_json['data']['stat']['like']
    # 收藏量
    favorite = res_json['data']['stat']['favorite']
    
    return title, desc, pubdata, tname, view, danmaku, coins, share, reply, like, favorite
