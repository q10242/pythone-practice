# coding=UTF-8
x = 100
print("x=/%6d/"% x)
y=10.5
print("y=/%6.2f/"%y)
s="Deep"
print("s=/%6s/"%s)

print "以下是保留隔數不足的範例"
print("x=/%2d/"% x)
print("y=/%1.0f/"%y)
print("s=/%3s/"%s)



print "以下是靠左顯示的範例"
print("x=/%-6d/"% x)
print("y=/%-6.2f/"%y)
print("s=/%-6s/"%s)

x=10
print("x=/%+6d/"% x)
print("y=/%+6.2f/"%y)
print("s=/%+6s/"%s)
