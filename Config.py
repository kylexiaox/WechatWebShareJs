__author__ = 'kyle_xiao'

import json
import random
import string

class Config(object):


    def __init__(self, fileName):
        """
        get the config of wechat public platform

        :param fileName: Config file path,

        """
        configfile = open(fileName)
        try:
            configText = configfile.read()
            configText = configText.replace('\n', '').replace(" ", "")
        finally:
            configfile.close()
        self.config = json.loads(configText)
        # add nonceStr to configurefe
        for co in self.config:
            if self.config[co]["nonceStr"] == "":
                self.config[co]["nonceStr"]=self.__create_nonce_str()



    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

