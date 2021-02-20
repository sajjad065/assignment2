total=int(input("How many string do you want to input in list "))
lis=[]
list_dub=[]
count=0
for i in range(total):
    str1=input("Enter strings ")
    lis.append(str1)
list_dub.append(lis[0])
for i in lis:     
    for j in list_dub: 
        if(i==j):
            count=count+1
    if(count>=1):
        count=0
    else:
        list_dub.append(i)
print("Original List: " +str(lis))                  
print("List with no dublicate: " +str(list_dub))       
           
 
