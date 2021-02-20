total=int(input("How many items do you want to input in list "))
lis=[]
count=0
for i in range(total):
    str1=input("Enter items  ")
    lis.append(str1)
print("original list is ")
print(lis)
copied_lis=lis
print("copied list is ")
print(copied_lis)
