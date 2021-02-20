total=int(input("How many elements in the dictionary "))
dic={}
count=0
for i in range(total):
    key1=input("Enter key ")
    value1=input("Enter value ")
    dic.update({key1:value1})
print("items in dictionary ", end='')
print(dic)
print("Only keys ")
for key, value in dic.items():
    print(key)
    
print("Only values ")    
for key, value in dic.items():
    print(value)
    
    
    
    
    
