__author__ = 'Andy'
#-*- coding:utf-8 -*-

import json
import urllib2

class DealShareInfo():
    def dealShareUrl(self, uk):
        url_uk = "http://pan.baidu.com/share/homerecord?uk="
        url_end = "&page=1&pagelength=60"
        return url_uk + uk + url_end

    def spiderSharedInfo(self, uk):

        url = self.dealShareUrl(uk)

        try:
            info = urllib2.urlopen(url, timeout=10).read()
        except Exception, e:
            print e
        json_dict = json.loads(info)
        share_list = json_dict['list']
        params_list = []
        if len(share_list) == 0:
            return params_list
        for tmp in share_list:
            param = ("'"+str(tmp['shareId'])+"'", "'"+tmp['typicalPath']+"'",\
                     "'"+r"http://pan.baidu.com/s/"+str(tmp['shorturl'])+"'", "'"+str(tmp['ctime'])+"')")
            params_list.append(','.join(param))

        return params_list