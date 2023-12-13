n = int(input("Enter the limit: "))
li = [] 
print("Enter the elements:")
for i in range(n):
    ele = int(input())
    li.append(ele)
print(li)
sum=0
for i in li:
	sum=sum+i
print("The sum of the list is :",sum)

