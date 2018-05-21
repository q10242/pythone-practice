x = 10

number1 = list(range(x));
print number1;


y = 16

number2 = list(range(x,y))
print number2

z = 2
number3 = list(range(x,y,z))
print number3

t = 0
for numbers in number3:
    t= t+numbers
else: #結束之後執行的區塊
    print "over!"


print t
