seq1=['a','b']
list_dict1=dict.fromkeys(seq1)
print("dict1:",list_dict1)
list_dict2=dict.fromkeys(seq1,'Chicago')


fruit={'apple':20,'banana':30}
a = fruit.get('apple')
print a
b = fruit.setdefault('orange')
print b
