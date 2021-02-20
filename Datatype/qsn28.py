total=int(input("How many elements do you want to input in dictionary "))
dic={}
for i in range(total):
    key1=input("Enter key:")
    val1=input("Enter value:")
    dic.update({key1:val1})
print("The dictionary list is :")
print(dic)
num=int(input("please input 1 if you want to add key to the given dictionary "))
if(num==1):
      total=int(input("How many elements do you want to input in the given dictionary "))
      for i in range(total):
          
          key2=input("Enter key:")
          val2=input("Enter value:")
          dic.update({key2:val2})
      
print("The final dictionary list is :")
print(dic)
    
      

