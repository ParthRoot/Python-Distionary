#get() return the element for specified key
dict = {
			"Name":"Parth",
			"Id":84
		}
print(dict.get("Name"))
print(dict.get("Id"))
for x in dict:
	print(dict.get(x))
	print(dict[x])
	