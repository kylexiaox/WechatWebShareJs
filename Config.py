__author__ = 'kyle_xiao'

import json
import random
import string

class Config(object):
    debug = str
    appId = str
    secret = str
    timestamp = str
    nonceStr = str
    signature1 = str  # for groupmessage
    signature2 = str  # for singlemessage
    signature3 = str  # for timelinemessage
    jsApiList = []
    url = str
    title = str
    subtitle = str
    imgUrl = str
    link = str


    def __init__(self, fileName):
        """
        get the config of wechat public platform

        :param fileName: Config file path,
        """
        configfile = open(fileName)
        try:
            configText = configfile.read()
            configText = configText.replace('\n', '').replace(" ", "")
            print(configText)
        finally:
            configfile.close()
        load = json.loads(configText)
        self.debug = load["debug"]
        self.appId = load["appId"]
        self.secret = load["secret"]
        if load["nonceStr"] == "":
            self.nonceStr = self.__create_nonce_str()
        else:
            self.nonceStr = load["nonceStr"]
        jsApiList = load["jsApiList"]
        for j in jsApiList:
            self.jsApiList.append(j.decode('utf-8'))
        self.url = load["url"]
        self.title = load["title"]
        self.subtitle = load["subtitle"]
        self.imgUrl = load["imgUrl"]
        self.link = load["link"]

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

