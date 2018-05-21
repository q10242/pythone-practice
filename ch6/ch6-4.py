str1=[1,2,3,4,5]
str2=[7,8,9,10]
str1.extend(str2)
print str1
print str2

#deep copy
str3 = str1
print str3
str1.append("100");
print str1
print str3
