# coding=utf-8
__author__ = 'kyle_xiao'
import time
from apiAccess import AccessTicket
import logging
from Config import Config

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class Auth(object):
    def __init__(self):
        """


        """
        self.config = Config("config")
        self.config.timestamp = 0.0
        self.js = None

    def updateJs(self):
        """
        generate new signature and new JS.

        """
        self.config.timestamp = time.time()
        signGenerator = AccessTicket(self.config.timestamp,self.config.appId,self.config.secret,self.config.nonceStr)
        self.config.signature1 = signGenerator.sign(self.config.url+"?from=groupmessage&isappinstalled=0")
        self.config.signature2 = signGenerator.sign(self.config.url+"?from=singlemessage&isappinstalled=0")
        self.config.signature3 = signGenerator.sign(self.config.url+"?from=timeline&isappinstalled=0")
        try:
             self.js = u"var signature;" \
                  "if(window.location.search=='?from=groupmessage&isappinstalled=0')" \
                  "signature = '{self.signature1}';" \
                  "else if(window.location.search=='?from=singlemessage&isappinstalled=0')" \
                  "signature = '{self.signature2}';" \
                  "else if(window.location.search=='?from=timeline&isappinstalled=0')" \
                  "signature = '{self.signature3}';" \
                  "" \
                  "wx.config({{" \
                  "debug: false," \
                  "appId: '{self.appId}'," \
                  "timestamp: {self.timestamp!s}, " \
                  "nonceStr: '{self.nonceStr}', " \
                  "signature: signature," \
                  "jsApiList: {self.jsApiList!r}" \
                  "}});" \
                  "" \
                  "wx.ready(function(){{" \
                  "wx.onMenuShareTimeline({{" \
                  "title: '{self.title}'," \
                  "link: '{self.url}'," \
                  "imgUrl: '{self.imgUrl}'," \
                  "success: function () {{" \
                  " " \
                  "}}," \
                  "cancel: function () {{" \
                  "" \
                  "}}" \
                  "}});" \
                  " wx.onMenuShareAppMessage({{" \
                  "title: '{self.title}'," \
                  "desc: '{self.subtitle}'," \
                  "link: '{self.url}'," \
                  "imgUrl: '{self.imgUrl}'," \
                  "type: '', " \
                  "dataUrl: ''," \
                  "success: function () {{ " \
                  " " \
                  "}}," \
                  "cancel: function () {{ " \
                  "" \
                  "}}" \
                  "}});"\
                  "}}" \
                 .format(self = self.config)
        except StandardError, e:
            logging.exception(e)
        print(self.js)

    def getJs(self):
        """
        provide the js file form
        after 7000 second, regenerate the new js file(for wechat update the key every 7200s)

        :return:  the js
        """
        if time.time()-self.config.timestamp >7000:
            self.updateJs()
        return self.js









