total=int(input("How many string do you want to input in list "))
lis=[]
count=0
for i in range(total):
    str1=input("Enter strings ")
    lis.append(str1)
if(total==0 or (len(lis)==0)):
    print("The list is empty")
else:
    print("The list is not empty")
