total=int(input("Enter total numbers "))
lis=[]
multiply=1
for i in range(total):
    num=int(input("Enter number "))
    lis.append(num)
lar=lis[0]  
for j in lis:
    if(j>lar):
        lar=j
print("The largest number is:" +str(lar))
           
 
