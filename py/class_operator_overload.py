class car:
	def __init__(self,name,price,km):
		self.name=name
		self.price=price
		self.km=km
	def __len__(self):
		return self.km
	def __add__(self,other):
		return self.price + other.price
n=input("Enter name :")
p=int(input("Enter price :"))
k=int(input("Enter kilometer :"))
car1=car(n,p,k)
n=input("Enter name :")
p=int(input("Enter price :"))
k=int(input("Enter kilometer :"))
car2=car(n,p,k)
print (len(car1))
print (car1+car2)

