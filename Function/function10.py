def even_numb(list1):
    even_list=[]
    for i in list1:
        if(i%2==0):
            even_list.append(i)
    print("Even Numbers in the list: "  +str(even_list))        

total=int(input("enter number of items in list "))
list=[]
for num in range(total):
    number=int(input("Enter Numbers "))
    list.append(number)
print("items you added in the list: "  +str(list))  
even_numb(list)    
            
