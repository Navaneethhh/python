n = int(input("Enter the limit: "))
li = [] 
print("Enter the elements:")
for i in range(n):
    ele = int(input())
    li.append(ele)
print(li)
for i in li:
	if(i%2==0):
		li.remove(i)
print(li)