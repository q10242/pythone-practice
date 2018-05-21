a = ('a' , 10 ,'b' , 20)
b = ('c' , 'd', 10 ,11 , 'x')
c = ('g','f','d','111')
print a,b;
zip = zip(a,b);
print zip
p = list(zip)
print p
print type(p)
x,y = zip( *p )
print x,y,z
