# WechatWebShareJs
share the web to wechat group or timeline
steps:
1.add wechat public account configure in configue file
2.run server in tornado and it will auto generate a wechat js file
3.import wechat jssdk and this js


PS: NEED TO ADD TYPE(TEXT_PLAIN AND TEXT_HTML) IN PYRESTFUL 


ABOUT CONFIG:

{"debug":"",                                                       # "true", "false"
 "appId":"",                                                       # wechat public APPID
 "secret":"",                                                      # wechat public SECRET
 "nonceStr":"",                                                    # RANDOM STRING, IF EMPTY, IT WILL AUTO GENERATE ONE
 "jsApiList":["onMenuShareTimeline","onMenuShareAppMessage"],      # API LIST
 "url":"",                                                         # URL WITH PREFIX "http://" or "https://"
 "title":"",                                                       # TITLE OF THE WEBSITE
 "subtitle":"",                                                    # ABSTRACT OF THE WEBSITE
 "link":"",                                                        # REF LINK
 "imgUrl":""}                                                      # IMG URL

 
