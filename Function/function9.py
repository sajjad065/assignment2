def prime_check(num):
    count=0
    if(num>=2):    
        for i in range(2,num):
            if(num%i==0):
                print(str(num)+" is not prime")
                count=count+1
                break
            else:
                continue
        if(count==0):
            print(str(num) +" is prime")  
    else:
         print(str(num)+" is not prime, enter number greater than 1")
number=int(input("enter number "))
prime_check(number)
