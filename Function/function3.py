def mul():
    total=int(input("Enter total numbers "))
    lis=[]
    multiply=1
    for i in range(total):
        num=int(input("Enter number "))
        lis.append(num)
    for j in lis:
        multiply=multiply*j
    print("Product of all numbers in the list is:")
    print(multiply)        
 
mul()
