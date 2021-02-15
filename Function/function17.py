str1=input("Enter any string:")
char=input("enter character to check:")
check_char=lambda x: True if x.startswith(char) else False
if(check_char(str1)):
    print(str1 +" :starts with character :" +char)
else:
        print(str1 +": does not starts with character: " +char)


                  
