a = (1, 2 ,3,4,5)
print a
b = ("apple","orange")
print b

c = (0,)
print c

d= (0,'G')
print d

for key in b:
    print key


b = ("dddd",)
print b

print "====================="


x = ('a','b','c','d','e')
print(x[1:3])
print(x[:2])
print(x[1:])
print(x[-2:])
print(x[1:5:2])



x[0]="asd"
print x

# tuple is just like list, can use function like list, but tuple cannot change the context inside,
# so any function that changes list is not able to use on tuble
