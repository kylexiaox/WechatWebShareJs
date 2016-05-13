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
        initial the Auth class as a singleton
        load the configure file
        and set the timestamp

        """
        self.config = Config("config").config
        for co in self.config:
            self.config[co]["timestamp"] = 0.0
            self.config[co]["js"]  = None

        self.substr_g = "?from=groupmessage&isappinstalled=0"
        self.substr_s = "?from=singlemessage&isappinstalled=0"
        self.substr_t = "?from=timeline&isappinstalled=0"
        print "configure initialed...."

    def updateJs(self,jsName):
        """
        generate new signature and new JS by the jsName.

        """
        currentConfig = self.config[jsName]
        currentConfig["timestamp"] = int(time.time())
        # fix the problem of unicode
        jsApiList = []
        for jsapi in currentConfig["jsApiList"]:
            jsApiList.append(jsapi.encode("utf-8"))

        # generate signature
        signGenerator = AccessTicket(currentConfig["timestamp"],
                                     currentConfig["appId"],
                                     currentConfig["secret"],
                                     currentConfig["nonceStr"])
        currentConfig["sign_group"] = signGenerator.sign(currentConfig["url"]+self.substr_g)
        currentConfig["sign_single"] = signGenerator.sign(currentConfig["url"]+self.substr_s)
        currentConfig["sign_timeline"] = signGenerator.sign(currentConfig["url"]+self.substr_t)

        #assemble js file
        try:
             currentConfig["js"] = u"var signature;" \
                  "if(window.location.search=='?from=groupmessage&isappinstalled=0')" \
                  "signature = {signature1};" \
                  "else if(window.location.search=='?from=singlemessage&isappinstalled=0')" \
                  "signature = '{signature2}';" \
                  "else if(window.location.search=='?from=timeline&isappinstalled=0')" \
                  "signature = '{signature3}';" \
                  "" \
                  "wx.config({{" \
                  "debug: {debug}," \
                  "appId: '{appId}'," \
                  "timestamp: {timestamp}, " \
                  "nonceStr: '{nonceStr}', " \
                  "signature: signature," \
                  "jsApiList: {jsApiList}" \
                  "}});" \
                  "" \
                  "wx.ready(function(){{" \
                  "wx.onMenuShareTimeline({{" \
                  "title: '{title}'," \
                  "link: '{url}'," \
                  "imgUrl: '{imgUrl}'," \
                  "success: function () {{" \
                  "{successCallback}" \
                  "}}," \
                  "cancel: function () {{" \
                  "{cancelCallback}" \
                  "}}" \
                  "}});" \
                  "wx.onMenuShareAppMessage({{" \
                  "title: '{title}'," \
                  "desc: '{subtitle}'," \
                  "link: '{url}'," \
                  "imgUrl: '{imgUrl}'," \
                  "type: '', " \
                  "dataUrl: ''," \
                  "success: function () {{ " \
                  "{successCallback}" \
                  "}}," \
                  "cancel: function () {{ " \
                  "{cancelCallback}" \
                  "}}" \
                  "}});"\
                  "}})" \
                 .format(signature1=currentConfig["sign_group"],
                         signature2=currentConfig["sign_single"],
                         signature3=currentConfig["sign_timeline"],
                         debug=currentConfig["debug"],
                         appId=currentConfig["appId"],
                         timestamp=currentConfig["timestamp"],
                         nonceStr=currentConfig["nonceStr"],
                         title=currentConfig["title"],
                         jsApiList=jsApiList,
                         url=currentConfig["url"],
                         imgUrl=currentConfig["imgUrl"],
                         successCallback=currentConfig["successCallback"],
                         cancelCallback=currentConfig["cancelCallback"],
                         subtitle=currentConfig["subtitle"],
                         )
        except StandardError, e:
            logging.exception(e)
        print("reload successful at "+jsName+" "+time.asctime( time.localtime(time.time()) ))

    def getJs(self,jsName):
        """
        provide the js file form
        after 7000 second, regenerate the new js file(for wechat update the key every 7200s)

        :return:  the js
        """
        if time.time()-self.config[jsName]["timestamp"] >7000:
            self.updateJs(jsName)
        return self.config[jsName]["js"]










