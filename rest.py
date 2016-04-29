__author__ = 'kyle_xiao'

import tornado.ioloop
import pyrestful.rest
from services import Auth

from pyrestful import mediatypes
from pyrestful.rest import get, post, put, delete


class WechatShareResource(pyrestful.rest.RestHandler):
    @get(_path="/H5/js", _produces=mediatypes.TEXT_PLAIN)
    def getShareJs(self):
        """
        start up a restful service that offer a js file that can
        link website to wechat offical account with desc and title

        :return:
        """
        return Auth().getJs()


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