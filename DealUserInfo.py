__author__ = 'Andy'
#-*- coding:utf-8 -*-

import json
import urllib2

class DealUserInfo():
    def dealUserUrl(self, uk):
        url_uk = "http://pan.baidu.com/pcloud/user/getinfo?bdstoken=null&query_uk="
        url_end = "&channel=chunlei&clienttype=0&web=1"
        return url_uk + uk + url_end

    def spiderUserInfo(self, uk):

        url = self.dealUserUrl(uk)

        try:
            info = urllib2.urlopen(url, timeout=10).read()
        except Exception, e:
            print e
        json_dict = json.loads(info)
        user_info_dict = json_dict['user_info']


        params = ("'"+str(user_info_dict['uk'])+"'", "'"+user_info_dict['uname']+"'", \
                  "'"+user_info_dict['avatar_url']+"'", "'"+str(user_info_dict['fans_count'])+"'", \
                  "'"+str(user_info_dict['follow_count'])+"'", "'"+str(user_info_dict['album_count'])+"'", \
                  "'"+str(user_info_dict['pubshare_count'])+"')")

        return ','.join(params)



