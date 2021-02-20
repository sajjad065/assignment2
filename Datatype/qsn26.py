total=int(input("How many elements do you want to input in list "))
lis=[]
new_list=[]
count=0
for i in range(total):
    val=input("Enter items:")
    lis.append(val)
print("The original list is ")
print(lis)    
st=input("Enter string you want to insert at the beginning of each items in the list: ")    
for j in lis:
    m=st+str(j)
    new_list.append(m)
    
print("The new list is: ")
print(new_list)
