dict1=[{'name':'ram','age':29,'address':'kathmandu'},{'name':'sabina','age':19,'address':'pokhara'},{'name':'nabin','age':41,'address':'butwal'},
       {'name':'sita','age':21, 'address':'dang'},{'name':'hari','age':38,'address':'lalitpur'}]
print("Original list of the dictionary ")
print(dict1)
dict1.sort(key=lambda x:x['address'])
print("dictionary after sorting address")
print(dict1)

dict1.sort(key=lambda x:x['age'])
print("dictionary based on age sorting")
print(dict1)

