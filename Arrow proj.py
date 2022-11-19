import time
import os
y=6
a=2
z=7
b=1
c=0
d=9
n=4
m=4
d=9
c=-1
while 1:
	temp=y
	y=a
	a=temp
	
	temp=z
	z=b
	b=temp
	
	temp=n
	n=c
	c=temp
	
	temp=m
	m=d
	d=temp 
	
	for i in range(9):
		for x in range(9):
			if(i==0)or(i==1)or(i==7)or(i==8):
				print(" ",end="")
			elif((i==2)or(i==6))and(x!=y):
				print(" ",end="")
			elif((i==2)or(i==6))and(x==y):
				print("*",end="")
			elif((i==3)or(i==5))and((x!=y)and(x!=z)):
				print(" ",end="")
			elif((i==3)or(i==5))and((x==y)or(x==z)):
				print("*",end="")
			elif(i==4)and((x>c)and(x<m)):
				print(" ",end="")
			elif(i==4)and(x==4):
				print("*",end="")
			elif(i==4)and((x>n)and(x<d)):
				print("*",end="")
		print("",end="\n")
	time.sleep(2)
	clear = lambda: os.system('cls')
	clear()


	
	for x in range(9):
		for i in range(9):
			if(i==0)or(i==1)or(i==7)or(i==8):
				print(" ",end="")
			elif((i==2)or(i==6))and(x!=y):
				print(" ",end="")
			elif((i==2)or(i==6))and(x==y):
				print("*",end="")
			elif((i==3)or(i==5))and((x!=y)and(x!=z)):
				print(" ",end="")
			elif((i==3)or(i==5))and((x==y)or(x==z)):
				print("*",end="")
			elif(i==4)and((x>c)and(x<m)):
				print(" ",end="")
			elif(i==4)and(x==4):
				print("*",end="")
			elif(i==4)and((x>n)and(x<d)):
				print("*",end="")
			
		print("",end="\n")

	
	time.sleep(2)
	clear = lambda: os.system('cls')
	clear()
	