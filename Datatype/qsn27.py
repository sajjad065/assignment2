total=int(input("How many elements do you want to input in first list "))
lis=[]
new_list=[]
modified_list=[]
for i in range(total):
    val=input("Enter items:")
    lis.append(val)

total1=int(input("How many elements do you want to input in second list "))

for i in range(total1):
    val1=input("Enter items:")
    new_list.append(val1)
for j in range(0,(total-1)):
    modified_list.append(lis[j])
   
print("The first list is ")
print(lis)    
print("The second list is ")
print(new_list)    
    
for k in range(0,(total1)):
    modified_list.append(new_list[k])
print("The modified list after removing last element from 1st list and adding 2nd list is :")
print(modified_list)      
