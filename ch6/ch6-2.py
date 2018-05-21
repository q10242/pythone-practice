james = [23,23,14,56,63]
#max
print max(james)
#min
print min(james)
#sum
print sum(james)

james = ['James',23,23,14,56,63]
print sum(james[1:])

print len(james)
james[0] = 1;

print sum(james)
james2 = ['apple' , 'banana']

james+= james2

print james
del james[-2]
print james


emptylist = []
emptylist += [1,3,4,]

print emptylist


del emptylist
print emptylist
