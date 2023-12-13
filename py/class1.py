class student:
	def __init__(self,name,rollno,course):
		self.name=name
		self.rollno=rollno
		self.course=course
	def display(self):
		print("Name is :"+self.name)
		print("Roll No is :",self.rollno)
		print("Course is :"+self.course)
n=input("Enter your name :")
r=int(input("Enter your roll no :"))
c=input("Enter your course")
std1=student(n,r,c)
print("\n")
n=input("Enter your name :")
r=int(input("Enter your roll no :"))
c=input("Enter your course :")
std2=student(n,r,c)
std1.display()
std2.display()
