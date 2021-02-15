str=input("Enter any String ")
length=len(str)
if(length<2):
    print("empty String")
else:
    first=str[0]
    second=str[1]
    last=str[length-1]
    secondlast=str[length-2]
    print(first+second+secondlast+last)
    
    
