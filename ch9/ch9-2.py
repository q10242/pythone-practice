solider0={'tag':'red','score': 3,'speed':'slow'}
solider1={'tag':'red','score': 5,'speed':'medium'}
solider2={'tag':'red','score':10,'speed':'slow'}
armys= [solider0,solider1,solider2]

for army in armys:
    print(army)


armys = []
for solider_number in range(50):
    solider={'tag':'red','score':3,'speed':'slow'}
    armys.append(solider)
for solider in armys[:3]:
    print solider
print len(armys)


for solider in armys[35:38]:
    print solider
    if solider['tag']=='red':
        solider['tag']='blue'
        solider['score']=10
        solider['speed']='medium'

print "------------"

for soldier in armys[35:40]:
    print solider


test={'a':['a','b','c'],'test':['ddddd','mmmmm']}
for gg in test:
    print("%s key is :" % gg)
    for elms in gg:
        print "    ",elms
