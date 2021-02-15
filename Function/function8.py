def unique(lis1):
    list2=[]
    list2.append(lis1[0])
    for j in lis1:
        if j in list2:
            continue;
        else:
            list2.append(j)
    print("List with unique items is given below")       
    print(list2)        

list1=[]
total=int(input("input total items in list "))
for i in range(total):
    number=input("Enter number in the list ")
    list1.append(number)
unique(list1)    
