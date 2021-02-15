total=int(input("Enter Total numbers in the list "))
list1=[]
for i in range(total):
                  num=int(input("Enter Numbers "))
                  list1.append(num)
print("Original list is :")
print(list1)
even=list(filter(lambda x:x%2==0, list1))
print("Even list is:")
print(even)
odd=list(filter(lambda x:x%2!=0, list1))
print("Odd list is:")
print(odd)      
                  
                  
