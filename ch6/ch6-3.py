str = " DeepStone "
print str
print str.upper()
print str.lower()
print str.title()
print "/"+str.lstrip()+"/"
print "/"+str.rstrip()+"/"
print "/"+str.strip()+"/"

print dir(str)

li = ['apple','banana','pineapple']
print li
li += 'orange'
print li

li.append('orange')
print li
li.insert(3,'grape')
print li
li.pop(4)
print li
li.remove('a')
print li
li.reverse()
print li

li.sort()
print li
li.reverse()

li2 = sorted(li)
print li
print li2
li2 = sorted(li,reverse=True)
print li2
li2 = sorted(li)
i = li2.index('orange')
print i
c = li2.count('apple')
print c

str2=['my','name','is','kurota']
sepchar = " "

print sepchar.join(str2)
sepchar = "\n"
print sepchar.join(str2)
