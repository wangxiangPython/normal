import codecs
import yaml

def ConfigHelp():
    with codecs.open('../conf/spiders.yaml', mode='r', encoding='utf-8') as config_file:
        config_dict = yaml.load(config_file,Loader=yaml.FullLoader)
    return config_dict

def get_proxies():
    pass

def get_userAgent():
    pass

if __name__ == '__main__':
    config = ConfigHelp()
    headers= config['bilibili_conf']['headers']
    print(headers)