from __future__ import print_function
# fstream1 = open("/Applications/MAMP/htdocs/python/ch4/out1.txt", mode ='w');
fstream1 = open("./out1.txt", mode ='w');
print("This is the message for file1",file=fstream1)
print("This is the message2 for file1",file=fstream1)
fstream1.close()
fstream2 = open("./out2.txt", mode ='a');
print("This is the message for file2",file=fstream2)
print("This is the message2 for file2",file=fstream2)
fstream2.close()
