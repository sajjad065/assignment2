str=input("Enter any String ")
char=str[0]
newstr=str[1:].replace(char,'$')
print(char+newstr)
