#!/usr/bin/python
# -*- coding: UTF-8 -*-
#简单使用try/except语句
#新建一个文件testfile，使用chmod -w testfile 去掉 testfile 文件的写权限


try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()
	
	
# 也可以写成try...finally语句
# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

# try:
    # fh = open("testfile", "w")
    # try:
        # fh.write("这是一个测试文件，用于测试异常!!")
    # finally:
        # print "关闭文件"
        # fh.close()
# except IOError:
    # print "Error: 没有找到文件或读取文件失败"