__author__ = 'Andy'
#-*- coding:utf-8 -*-

import json
import urllib2
class DealFansInfo():

    #拼接要爬取的URL地址
    def dealFansUrl(self, uk, start = 0):
        url_uk = "http://pan.baidu.com/pcloud/friend/getfanslist?query_uk="
        url_start = "&limit=24&start="
        url_end = "&bdstoken=null&channel=chunlei&clienttype=0&web=1"
        return url_uk + uk + url_start + str(start) + url_end

    #读取对应的URL数据
    def getPageInfo(self, url):

        try:
            info = urllib2.urlopen(url, timeout=10).read()
        except Exception, e:
            print e

        return info

    def spiderFansInfo(self, uk):
        #获取首页信息
        url = self.dealFansUrl(uk)
        info = self.getPageInfo(url)

        json_dict = json.loads(info)
        fans_list = json_dict['fans_list']
        fans_num = json_dict['total_count']

        params_list = []
        fans_uks_list = []
        fans_uk_list = []
        for tmp in fans_list:
            params = ("'"+ uk +"'", "'"+str(tmp[u'fans_uk'])+"'", "'"+tmp[u'fans_uname']+"'", "'"+str(tmp[u'avatar_url'])+"'", "'"+str(tmp[u'is_vip'])+"'",\
                      "'"+str(tmp[u'fans_count'])+"'", "'"+str(tmp[u'follow_count'])+"'", "'"+str(tmp[u'pubshare_count'])+"'",\
                      "'"+str(tmp[u'follow_time'])+"')")
            fans_uk_list.append("("+str(tmp[u'fans_uk'])+")")
            params_list.append(','.join(params))
        fans_uks_list.append(','.join(fans_uk_list))

        #判断是否粉丝页只有一页
        if fans_num < 24:
            return params_list, fans_uks_list

        page_num = 0
        if (fans_num%24 != 0) and (fans_num/24 > 0):
            page_num = fans_num/24 + 1
        else:
            page_num = fans_num/24

        #循环遍历粉丝页
        for num in range(1, page_num):
            fans_uk_list2 = []
            url = self.dealFansUrl(uk, num*24)

            info = self.getPageInfo(url)
            json_dict = json.loads(info)
            fans_list = json_dict['fans_list']

            for tmp in fans_list:
                params = ("'"+ uk +"'", "'"+str(tmp[u'fans_uk'])+"'", "'"+tmp[u'fans_uname']+"'", "'"+str(tmp[u'avatar_url'])+"'", "'"+str(tmp[u'is_vip'])+"'",\
                          "'"+str(tmp[u'fans_count'])+"'", "'"+str(tmp[u'follow_count'])+"'", "'"+str(tmp[u'pubshare_count'])+"'",\
                          "'"+str(tmp[u'follow_time'])+"')")
                params_list.append(','.join(params))
                fans_uk_list2.append("("+str(tmp[u'fans_uk'])+")")
            fans_uks_list.append(','.join(fans_uk_list2))
        return params_list, fans_uks_list

