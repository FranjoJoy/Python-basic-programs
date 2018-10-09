#MENU DRIVEN CALCULATOR

def add(x,y):
	add=x+y
	print x,"+",y,"=",add
def sub(x,y):
	sub=x-y
	print x,"-",y,"=",sub
def mult(x,y):
	mult=x*y
	print x,"x",y,"=",mult
def div(x,y):
	div=x/y
	print x,"/",y,"=",div
def exp(x,y):
	exp=x**y
	print x,"^",y,"=",exp

print "MENU"
print "1.Addition"
print "2.Subtraction"
print "3.Multiplication"
print "4.Division"
print "5.Exponential"
choice=input("Enter the choice")
if choice==1:
	a=input("Enter the first number")
	b=input("Enter the second number")
	add(a,b)
elif choice==2:
	a=input("Enter the first number")
	b=input("Enter the second number")
	sub(a,b)
elif choice==3:
	a=input("Enter the first number")
	b=input("Enter the second number")
	mult(a,b)
elif choice==4:
	a=input("Enter the first number")
	b=input("Enter the second number")
	div(a,b)
elif choice==5:
	a=input("Enter the first number")
	b=input("Enter the second number")
	exp(a,b)
else:
	print "ivalid selection"


