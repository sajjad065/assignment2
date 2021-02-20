total=int(input("How many elements in the dictionary "))
dic={}
count=0
for i in range(total):
    key1=input("Enter key ")
    value1=input("Enter value ")
    dic.update({key1:value1})
key_word=input("Enter key you want to search ")
for key, value in dic.items():
    if(key==key_word):
        print("The key exists :")
        count=count+1
        break
if(count==0):
     print("The key does not exists:")
    
    
    
