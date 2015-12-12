#-*- coding:utf-8 -*-

import sys
import traceback
import Logger

def printExceptTrace():
    info = sys.exc_info()
    logs = []
    logs.append('[EXCEPTION]Traceback as below:')
    for fname, lineno, function, text in traceback.extract_tb(info[2]):
        if fname.lower().startswith('c:\\python27'):
            continue
        logs.append('%s line %s in %s()' % (fname, lineno, function))
        logs.append('  => %s' % repr(text))
        logs.append('  ** %s: %s' % info[:2])
    Logger.Logger.Write('\n'.join(item for item in logs))
    
def printExceptTraceEx(md5):
    info = sys.exc_info()
    logs = []
    logs.append('[EXCEPTION][%s]Traceback as below:' % md5.lower())
    for fname, lineno, function, text in traceback.extract_tb(info[2]):
        if fname.lower().startswith('c:\\python27'):
            continue
        logs.append('%s line %s in %s()' % (fname, lineno, function))
        logs.append('  => %s' % repr(text))
        logs.append('  ** %s: %s' % info[:2])
    Logger.Logger.Write('\n'.join(item for item in logs))