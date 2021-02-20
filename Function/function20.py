array1=[1,2,3,4,6,7,8,9]
array2=[5,6,8,9,12]
print("originals arrays:")
print(array1)
print(array2)
res=list(filter(lambda x:x in array1,array2))
print("Intersection:",res)
