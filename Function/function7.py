def check_in(str1):
    upper=0
    lower=0
    for i in str1:
        if(i.islower()):
            lower=lower+1
        elif(i.isupper()):
            upper=upper+1
    print("total upper case:" +str(upper))
    print("total lower case:" +str(lower))
    
str1=input("Enter String ")
check_in(str1)
