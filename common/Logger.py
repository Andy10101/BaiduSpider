#-*- coding: utf-8 -*-

import datetime
import time
import os
import threading

def thread_safe(func):
    '''函数线程安全装饰器'''
    mutex = threading.Lock() # 新建锁
        
    def dec(*args, **kwargs):
        '''装饰函数'''
        mutex.acquire() # 请求获得锁
        try:
            result = func(*args, **kwargs) # call 原函数
        finally:
            mutex.release() # 释放锁
        return result
    return dec

class Logger(object):
    '''
    logger.
    '''
    @classmethod
    @thread_safe
    def Write(cls, msg):
        try:
            #log_dir = os.path.join('/usr/local/src/yumdownload/MoveData', 'log')
            log_dir = os.path.join(os.getcwd(), 'log')
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            
            try:
                log_path = log_dir + '/' + str(datetime.date.today()) + '.py.log'
                log_file = open(log_path, 'a')
                msg_l = '[%s]%s\n' % (time.ctime(time.time()), msg)
                if isinstance(msg_l, unicode):
                    print msg_l.encode('gbk')
                else:
                    print unicode(msg_l, 'utf-8').encode('gbk')
                log_file.write(msg_l)
                log_file.close()
            except Exception, ex:
                print '[%s][Logger] Error: cannot write log!' % (time.ctime(time.time())), ex
        except Exception, ex:
            print '[%s][Logger] Error: cannot create log path!' % (time.ctime(time.time())), ex
            
    @classmethod
    @thread_safe
    def WriteLogOnly(cls, msg):
        try:
            log_dir = os.path.join('/usr/local/src/yumdownload/MoveData', 'log')
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            
            try:
                log_path = log_dir + '/' + str(datetime.date.today()) + '.py.log'
                log_file = open(log_path, 'a')
                msg_l = '[%s]%s\n' % (time.ctime(time.time()), msg)
                log_file.write(msg_l)
                log_file.close()
            except Exception, ex:
                print '[%s][Logger] Error: cannot write log!' % (time.ctime(time.time())), ex
        except Exception, ex:
            print '[%s][Logger] Error: cannot create log path!' % (time.ctime(time.time())), ex
            
    @classmethod
    @thread_safe
    def WriteEx(cls, md5, msg):
        try:
            log_dir = os.path.join('/usr/local/src/yumdownload/MoveData', 'log')
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            
            try:
                log_path = log_dir + '/' + str(datetime.date.today()) + '.py.log'
                log_file = open(log_path, 'a')
                msg_l = '[%s][%s]%s\n' % (time.ctime(time.time()), md5, msg)
                if isinstance(msg_l, unicode):
                    print msg_l.encode('gbk')
                else:
                    print unicode(msg_l, 'utf-8').encode('gbk')
                log_file.write(msg_l)
                log_file.close()
            except Exception, ex:
                print '[%s][Logger] Error: cannot write log!' % (time.ctime(time.time())), ex
        except Exception, ex:
            print '[%s][Logger] Error: cannot create log path!' % (time.ctime(time.time())), ex
            
if __name__ == '__main__':
    str1 = '[%s][FtpHelper] Error! Create file \n--> "%s"\n-->failed!' % (time.ctime(time.time()), 'abc')
    Logger.Write(str1)