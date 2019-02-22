#!/usr/bin/python2

# writing file 


# reading file 

f=open('/root/Desktop/hii.txt')   #  read 
print  f.read()
f.close()

#  mod

with  open('/root/Desktop/hii.txt','r')  as   f:
	print f.read()
#  close automated 
