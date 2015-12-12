#-*- coding:utf8 -*-
__author__ = 'Andy'

import MySQLdb
import TracebackLog

class MySqlHelper():
    def __init__(self, ip, port, db, usr, psw):
        self.db = None
        self.db_cfg = [ip,port , db, usr, psw]

    def Connect(self):
        ''' Connect to remote database
        '''
        ret = 0
        try:
            self.db = MySQLdb.Connect(host = self.db_cfg[0],
                                        port = self.db_cfg[1],
                                        db = self.db_cfg[2],
                                        user = self.db_cfg[3],
                                        passwd = self.db_cfg[4],
                                        charset='utf8')
            ret = 1
        except:
            TracebackLog.printExceptTrace()
        return ret

    def CloseDB(self):
        '''Close database Connection
        '''
        if self.db != None:
            self.db.close()
            self.db = None

    def ExecuteSql(self, sql, params, many=False, commit=False):
        '''Execute sql.
        many: insert or update or delete by muti-conditions.
              used ONLY when need change data (insert, update, delete)
        commit: used ONLY when need change data (insert, update, delete)
        '''
        ret = 0
        cds = ()
        bConnected = False
        # 1. 确认连接是否成功
        if self.db == None:
            bConnected = self.Connect()
        else:
            try:
                self.db.ping()
                bConnected = True
            except MySQLdb.OperationalError:
                if self.db == self.db:
                    self.Connect()
                    self.db = self.db
            except Exception:
                TracebackLog.printExceptTrace()
        try:
            cursor = self.db.cursor()
            if many:
                ret = cursor.executemany(sql, params)
            else:
                ret = cursor.execute(sql, params)
            if commit:
                self.db.commit()
            else:
                cds = cursor.fetchall()
            cursor.close()
        except Exception, ex:
            print '[Exec sql exception] %s' % str(ex)
            print sql
            print params
            if commit:
                self.db.rollback()
        return ret, cds