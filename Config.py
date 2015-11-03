__author__ = 'kyle_xiao'

import json


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
        self.nonceStr = load["nonceStr"]
        self.jsApiList = load["jsApiList"]
        self.url = load["url"]
        self.title = load["title"]
        self.subtitle = load["subtitle"]
        self.imgUrl = load["imgUrl"]
        self.link = load["link"]


