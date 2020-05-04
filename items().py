#items() used to return key and value pair
#Returns a list containing a tuple for each key value pair
dict = {
			"Name":"Parth",
			"Id":84
		}
print(dict.items())
z = dict.items()
print(type(z))
for x,y in dict.items():
	print(x,y)
	print(dict.items())