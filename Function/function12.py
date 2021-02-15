def mul(num):
    return lambda x:x*num
product=mul(2)
a=int(input("enter number to multiply with unknown number "))
print("The product is "+ str(product(a)))
