class rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b
	def d(self):
		print("The area is :",l*b)
		
		print("The peremeter is :",(2*(l+b)))
l=int(input("Enter the length :"))
b=int(input("Enter the breadth :"))
r1=rectangle(l,b)
r1.d()