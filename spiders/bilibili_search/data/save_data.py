import csv
import time


def save(spider_name,save_time,total_info):
    file_path = '../data/crawl_data/{}_{}.csv'.format(spider_name,save_time)
    # file_path = './crawl_data/{}_{}.csv'.format(spider_name,save_time)
    with open(file_path,'a+',encoding='utf-8-sig',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(total_info)

if __name__ == '__main__':
    save('xiaohongshu',2020,[[1]])