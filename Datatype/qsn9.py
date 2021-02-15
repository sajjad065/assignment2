str=input("enter string ")
print("you entered " +str)
length=len(str)
first_char=str[0]
last_char=str[(length-1)]
swapped_str=last_char+str[1:-1]+first_char
print("The modified string is :" +swapped_str)
