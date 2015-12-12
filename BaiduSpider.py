__author__ = 'Andy'
#-*- coding:utf-8 -*-
import time
from DealUserInfo import DealUserInfo
from DealFansInfo import DealFansInfo
from DealShareInfo import DealShareInfo
from common import MySqlHelper

class GetInfo():

    def __init__(self):
        self.baidu_db = MySqlHelper.MySqlHelper('数据链接地址', 3306, 'baidu', 'baidu', 'baidu')

    def insertUserInfo(self, uk_list):
        userobj = DealUserInfo()
        sql_start = "insert into user_info (uk, uname, avatar_url, " \
                    "fans_count, follow_count,album_count, pubshare_count) values ("
        for tmp in uk_list:
            sql_end = userobj.spiderUserInfo(tmp)
            sql = sql_start + sql_end
            params = None
            if len(sql_end) != 0:
                self.baidu_db.ExecuteSql(sql, params, False, True)

    def insertShareInfo(self, uk_list):
        shareobj = DealShareInfo()
        sql_start = "insert into share_info (shareuk, sharefile, shareturl, sharetime) values ("
        for tmp in uk_list:
            sql_end_list = shareobj.spiderSharedInfo(tmp)
            for sql_end in sql_end_list:
                sql = sql_start + sql_end
                params = None
                if len(sql_end) != 0:
                    self.baidu_db.ExecuteSql(sql, params, False, True)

    def insertFansInfo(self, url_list):

        for url in url_list:

            fansobj = DealFansInfo()
            fans_list, fans_uk_list = fansobj.spiderFansInfo(url)

            for sql_end in fans_list:
                sql_start = "insert into fans_list (uk, fans_uk, fans_name, fans_avatar_url, is_vip, fans_count, " \
                      "follow_count, pubshare_count, follow_time) values ("

                sql = sql_start + sql_end
                params = None
                self.baidu_db.ExecuteSql(sql, params, False, True)

            for fan_uk in fans_uk_list:
                sql = "INSERT into uk_list(uk) VALUES " + fan_uk
                params = None
                self.baidu_db.ExecuteSql(sql, params, False, True)


    def dealUk(self, uk_tuple):
        uk_list = []
        uk_list_str = []
        for tmp in uk_tuple:
            uk_list.append(tmp[0].strip())
            uk_list_str.append("'"+tmp[0].strip()+"'")

        return ','.join(uk_list), uk_list


    def Start(self):

        self.baidu_db.Connect()

        try:
            while True:
                #选取需要爬去的UK
                sql = "SELECT uk FROM uk_list WHERE flag = 0 LIMIT 10"
                params = None
                course = self.baidu_db.ExecuteSql(sql, params, False, False)
                if course[0] == 0:
                    print "The database has no need to take up UK"
                    time.sleep(10)
                    continue

                #标记已选取的UK
                uk_tuple = course[1]
                sql_uk, uk_list = self.dealUk(uk_tuple)
                sql_update = "UPDATE uk_list SET flag = 1 WHERE uk in (" + sql_uk + ")"
                self.baidu_db.ExecuteSql(sql_update, params, False, False)

                self.insertUserInfo(uk_list)
                self.insertShareInfo(uk_list)
                self.insertFansInfo(uk_list)
                sql_update = "UPDATE uk_list SET flag = 2 WHERE uk in (" + sql_uk + ")"
                self.baidu_db.ExecuteSql(sql_update, params, False, False)

        except Exception, e:
            print e
        finally:
            self.baidu_db.CloseDB()



if __name__ == "__main__":
    obj = GetInfo()
    obj.Start()
