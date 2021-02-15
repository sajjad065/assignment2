str=input("enter string ")
print("you entered " +str)
result=""
length=len(str)
for i in range(length):
    if(i%2==0):
        result=result+str[i]
print("new string having only even index is :" +result)
