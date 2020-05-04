#Nested Dictionary
print("Nested Dictionary")
Students = {
			"Parth":{
					"Name":"Parth Patel",
					"RollNo":84
					},
			"Jaimin":{
					 "Name":"Jaimin Patel",
					 "RollNo":85
					 },
			"Varshil":{
					   "Name":"Varshil Patel",
					   "RollNo":86
					  }
			}
for x in Students.items():
	print(x)
print("\r")
for x,y in Students.items():
	print(x,y)
print("\r")
for x in Students:
	print(x)

dict=dict(A="Apple",B="Banana",O="Orange")
print(dict)
	

	
	
