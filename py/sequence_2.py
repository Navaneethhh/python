n=int(input("Enter the limit :"))
for i in range(1,n+1):
	for j in range(1,i+1):
		print("*",end="")
	print("\r")
for i in range(1,n+1):
	for j in range(i,n):
		print("*",end="")
	print("\r")