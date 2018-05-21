drinks = {"coffee","tea","wine"}
enu = enumerate(drinks)

for elm in enu:
    print elm
else:
    print "done!"


for elm in enu: #not execute
    print elm
else:
    print "done!!"


for a,b in enumerate(drinks):
    print a,b
else:
    print "done~"
