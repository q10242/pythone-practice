a= {"a":"b" , "c":"d", "a":"d"}
print a
print a['c']
a['a'] = 'changed'
print a
del a['a']
print a

print a.clear()
a['b'] = "ddddd"
print a
x = a.copy()
print x
y = 'b' in x
print y

x['c'] = "prepare"

for key,value in x.items():
    print key
    print value
else:
    print "done"



for key in x:
    print key
    print x[key]
else:
    print "done2"

for values in x.values():
    print value
print "done3"
