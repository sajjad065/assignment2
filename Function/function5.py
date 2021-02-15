def fac(num):
    fact=1;
    if(num<0):
        print(int("Please  enter non-negative number"))
    else:
        for i in range(1,(num+1)):
            fact=fact*i
        print("The factorial is: ")
        print(fact)
number=int(input("Enter number "))
fac(number)

