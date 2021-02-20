n=int(input("Enter number from 1 to any natural number:"))
dic={}
for i in range(1,(n+1)):
    key1=i
    value1=i*i
    dic.update({key1:value1})
print("items in dictionary ")
print(dic)
