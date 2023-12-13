def sum(x,y):
	s=x+y
	return s
def dif(x,y):
	s=x-y
	return s
def mul(x,y):
	s=x*y
	return s
def div(x,y):
	s=x/y
	return s
a=int(input("Enter the frst no:"))
b=int(input("Enter the scnd no:"))
c=sum(a,b)
d=dif(a,b)
e=mul(a,b)
f=div(a,b)
print("The sum of the numbers is :",c)
print("The difference of the numbers is :",d)
print("The product of the numbers is :",e)
print("The reminder of the numbers is :",f)
