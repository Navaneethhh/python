class car:
	def __init__(self,name,price,colour):
		self.name=name
		self.price=price
		self.colour=colour
	def display(self):
		print("Name of the car is :"+self.name)
		print("Price of the car is :",self.price)
		print("Colour of the car is :"+self.colour)
n=input("Enter name of the car :")
r=int(input("Enter price of the car :"))
c=input("Enter colour of the car :")
car1=car(n,r,c)
print("\n")
n=input("Enter name of the car :")
r=int(input("Enter price of the car :"))
c=input("Enter colour of the car :")
car2=car(n,r,c)
car1.display()
print("\n")
car2.display()
