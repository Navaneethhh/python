class student:
	def __init__(self,name,rollno,course):
		self.name=name
		self.rollno=rollno
		self.course=course
	def display(self):
		print("Name is :"+self.name)
		print("Roll No is :",self.rollno)
		print("Course is :"+self.course)
class test(student):
	def __init__(self,mark1,mark2):
		self.mark1=mark1
		self.mark2=mark2
	def testdis(self):
		print("Mark 1 is :",self.mark1)
		print("Mark 2 is :",self.mark2)
class grade(test):
	def __init__(self,mark1,mark2):
		self.mark1=mark1
		self.mark2=mark2
	def gradedis(self):
		t=self.mark1
		if(101>t>=50):
			print("A grade")
		elif(0<=t<=50):
			print("B grade")
n=input("Enter your name :")
r=int(input("Enter your roll no :"))
c=input("Enter your course :")
m1=int(input("Enter your mark 1 :"))
m2=int(input("Enter your mark 2 :"))
std1=student(n,r,c)
test1=test(m1,m2)
grd1=grade(m1,m2)
print("\n")
std1.display()
test1.testdis()
grd1.gradedis()
