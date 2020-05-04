# Create Python Distionaries
Student = {
			"ID":176230316084,
			"FirstName":"Parth",
			"LastName":"Patel",
			"Branch":"Information Technology",
			"SEM":6
	  }
	  
#Accessing the items
print("ID:-",Student["ID"])

#Using the get() method	
x = Student.get("FirstName")
y = Student.get("LastName")
z = Student.get("Branch")
w = Student.get("SEM")
print("FirstName:-",x,"\nLastName:-",y,"\nBranch:-",z,"\nSEM:-",w)

#Print Value one by one
for x in Student:
	print(x,":-",Student[x])
print("\n")

#Using The values() Method
print("Without values Method")
for x in Student:
	print(x)
	
print("\n")
	
print("With values Method")
for x in Student.values():
	print(x)
	
print("\r")

print("Using the items() method")
for x,y in Student.items():
	print(x,y)
print("\r")

#Let's Check ID is present in Destionary or not
print("Determing ID is present in Student")
if "ID" in Student:
	print(True)
else:
	print(False)
#Find the length of Distionaries
print("Student Length:-",len(Student))

#Distionary Constructor
cons = dict(Car="Waganor",Bike="Hero Splendar")
print(cons)
