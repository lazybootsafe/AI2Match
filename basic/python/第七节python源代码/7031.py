#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 示例为成员运算符演示程序
 
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
 
if ( a in list ):
   print "1 - 变量 a 在给定的列表中 list 中"
else:
   print "1 - 变量 a 不在给定的列表中 list 中"
 
if ( b not in list ):
   print "2 - 变量 b 不在给定的列表中 list 中"
else:
   print "2 - 变量 b 在给定的列表中 list 中"
 
# 修改变量 a 的值
a = 2
if ( a in list ):
   print "3 - 变量 a 在给定的列表中 list 中"
else:
   print "3 - 变量 a 不在给定的列表中 list 中"
   
   
   
   
   
# 运算结果：
# 1 - 变量 a 不在给定的列表中 list 中
# 2 - 变量 b 不在给定的列表中 list 中
# 3 - 变量 a 在给定的列表中 list 中