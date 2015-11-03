__author__ = 'kyle_xiao'
import tornado.httpclient
import urllib
import json
import hashlib


class AccessTicket(object):
    def __init__(self, timestamp, appId, key, nonceStr):
        """

        :param timestamp:
        :param appId:
        :param key:
        :param nonceStr:
        """
        self.appId = appId
        self.key = key
        self.ret = {
            'nonceStr': nonceStr,
            'jsapi_ticket': self.getTicket(),
            'timestamp': timestamp,
            'url': ""
        }

    def getAccessToken(self):
        """
        get the wechat access_token

        :return:
        """
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("https://api.weixin.qq.com/cgi-bin/token?" + \
                                urllib.urlencode(
                                    {"grant_type": "client_credential", "appid": self.appId, "secret": self.key}))
        body = json.loads(response.body)
        return body["access_token"]

    def getTicket(self, token=None):
        """
        get the access ticket by using the token
        :param token:
        :return:
        """
        if token == None:
            token = self.getAccessToken()
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("https://api.weixin.qq.com/cgi-bin/ticket/getticket?" + \
                                urllib.urlencode({"access_token": token, "type": "jsapi"}))
        body = json.loads(response.body)
        return body["ticket"]

    def sign(self, url):
        """
        config one url to the wechat share
        :param url:
        :return:
        """
        self.ret["url"] = url
        string = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
        print string
        return hashlib.sha1(string).hexdigest()
