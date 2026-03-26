name=input("Enter your name: ")
usn=input("Enter your usn: ")
marks1=int(input("Enter the marks of subject 1: "))
marks2=int(input("Enter the marks of subject 2: "))
marks3=int(input("Enter the marks of subject 3: "))
marks=marks1+marks2+marks3
percentage=marks/3
print("**************STUDENT DETAILS**************")
print("Name: "+name)
print("USN: "+usn)
print("Total Marks: "+ str(marks))
print("Percentage: "+str(percentage))


