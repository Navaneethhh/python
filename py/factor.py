a=int(input("Enter the number :"))
b=a//2
print("The factors are:")
for i in range(1,b+1):
	if(a%i==0):
		print(  i)
print(a)

