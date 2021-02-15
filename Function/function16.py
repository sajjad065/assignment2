total=int(input("Enter Total numbers in the list "))
list1=[]
for i in range(total):
                  num=int(input("Enter Numbers "))
                  list1.append(num)
print("Original list is :")
print(list1)
square=list(map(lambda x:x**2, list1))
print("Square list is:")
print(square)
cube=list(map(lambda x:x**3, list1))
print("Cube list is:")
print(cube)      
                  
                  
