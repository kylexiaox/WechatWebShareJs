__author__ = 'kyle_xiao'

import tornado.ioloop
import tornado.web
import pyrestful.rest
from services import Auth
import time
from pyrestful import mediatypes
from pyrestful.rest import get, post, put, delete


class WechatShareResource(pyrestful.rest.RestHandler):
    @get(_path="/H5/{name}", _produces=mediatypes.TEXT_PLAIN)
    def getShareJs(self,name):
        """
        start up a restful service that offer a js file that can
        link website to wechat offical account with desc and title

        :return:
        """
        try:
            js = Auth().getJs(jsName=name)
            print "Request: successfully load js: "+name+" "+time.asctime(time.localtime(time.time()))
            return js
        except Exception,e:
            raise tornado.web.HTTPError(404)


# start tornado server
if __name__ == '__main__':
    try:
        print "Start the service"
        service = [WechatShareResource]
        app = pyrestful.rest.RestService(service)
        app.listen(8765)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print "\nStop the service"