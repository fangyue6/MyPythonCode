#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月10日

@author: fangyue
'''
def fun1():
    try:
        1/0
    except Exception:
        print 'zero'
    
def safe_float(obj):
    'safe version of float()'
    try:
        retval=float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    return retval

print safe_float([2.0,56.0,56,'dd'])
print safe_float('dd')

def main():
    'handles all the data processing'
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
    except IOError, e:
        log.write('no txns this month\n')
        log.close()
        return
    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')
    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result, float):
             total += result
             log.write('data... processed\n')
        else:
            log.write('ignored: %s' % result)
            print '$%.2f (new balance)' % (total)
            log.close()
        
if __name__ == '__main__':
         main()




