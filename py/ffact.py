def fact(x):
	s=1
	for i in range(1,x+1):
		s=s*i
	return s
n=int(input("Enter the number:"))
print(fact(n))