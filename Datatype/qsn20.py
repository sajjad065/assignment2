total=int(input("How many string do you want to input in list "))
lis=[]
count=0
for i in range(total):
    str1=input("Enter strings ")
    lis.append(str1)
for j in lis:
    if(len(j)>2 and (j[0]==j[-1])):
       count=count+1
print("The number of string with lenth  2 or more and having same first and last character is equal to :" +str(count))       
           
 
