tuple1=[('ram',29),('sabina',19),('nabin',41),('sita',21),('hari',38)]
print("Original list of the tuple ")
print(tuple1)
tuple1.sort(key=lambda x:x[1])
print("tuple after sorting")
print(tuple1)

