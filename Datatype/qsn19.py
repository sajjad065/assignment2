total=int(input("Enter total numbers you want to input in list"))
lis=[]
for i in range(total):
    num=int(input("Enter number "))
    lis.append(num)
small=lis[0]  
for j in lis:
    if(j<small):
        small=j
print("The smallest number is:" +str(small))
           
 
