str=input("Enter any String ")
not_index=str.find("not")
poor_index=str.find("poor")
if(not_index<poor_index):
   print( str.replace(str[not_index:(poor_index+4)],"good"))

else:
    print(str)

