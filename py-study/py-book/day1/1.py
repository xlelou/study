#!/usr/bin/python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 单独执行和在交互解释器中执行的区别
1+2*4

# 输入一段字符串，换成Int行
# test = raw_input('enter:')
# print test


# while 和 for range 输出0-10
# num = 0
# while num <=10:
#     print num
#     num +=1
#
# for i in range(0,11):
#     print i

# 判断正负
# test  =  raw_input('enter：')
# test = int(test)
# if test > 0:
#     print 'bigger than 0'
# elif test == 0:
#     print 'is 0'
# else:
#     print 'lower than 0'

#逐字显示
# test = raw_input('enter:')
# num = 0
# while num < len(test):
#     print test[num]
#     num +=1
#
# for i in range(len(test)):
#     print test[i]

#输入求和
# test = []
# a = 0
# for i in range(5):
#     aa = raw_input('enter:')
#     print aa
#     test.append(aa)
# for i in test:
#      a = a + int(i)
#
# print a/5


#显示选项菜单
# def aa():
#     print '''
#         1.asd
#         2.das
#         3.asdasd
#         请输入您的选项
#     '''
#     num = raw_input('enter:')
#     def asd():
#         test = []
#         a = 0
#         for i in range(5):
#             aa = raw_input('enter:')
#             print aa
#             test.append(aa)
#         for i in test:
#             a = a + int(i)
#
#         print a / 5
#     if num == '1':
#         asd()
#         aa()
#
#     elif num =='2':
#         exit()
# aa()

print dir(sys)
