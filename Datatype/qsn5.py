str=input("Enter first String ")
length=len(str)
if(length<3):
    print(str)
elif(str[(length-3):]=="ing"):
     print( str.replace("ing","ly"))
else:
    print(str+"ing")
