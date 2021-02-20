total=int(input("How many elements do you want to input in dictionary "))
dic={}
count=0
for i in range(total):
    key1=input("Enter key:")
    value1=input("Enter value:")
    dic.update({key1:value1})
for j in dic:
    if(j!=""):
        count=count+1
        break
        
if (bool(dic) and count!=0) :
    print("The dictionary is  not empty ")
else:
    print("The dictionary is empty")
