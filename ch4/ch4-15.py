#coding=UTF-8
from __future__ import print_function

name = input("請輸入姓名：")
grade = input("請輸入成績：")

print("the type of name is " , type(name))
print("the type of grade is " , type(grade))


clastname = input("請輸入中文姓氏")
cfirstname = input("請輸入中文名字")
cfullname = clastname +cfirstname
print("%s 歡迎使用本系統" % cfullname)
