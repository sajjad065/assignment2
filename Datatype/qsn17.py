list1=[]
multiply=1
total=int(input("Please input the total numbers to be added in the list "))
for n in range(total):
     number=int(input("enter number "))
     list1.append(number)
for j in list1:
        multiply=multiply*j
print("Product of all numbers in the list is:")
print(multiply)        
 

