




### lamda functions###

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

######

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


        
###find the odd number from the list ####

old_list=[2,4,5,6,10,15]
new_list=list(filter(lambda x:(x%2!=0),old_list))
print(old_list)
print(new_list)


        
###write a program to find the sum of 2 numbers using lambda###

m=int(input("enter the 1st number"))
n=int(input("enter the 2nd number"))
sum=m+n
print("sum :",sum)
