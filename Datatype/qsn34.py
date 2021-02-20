n1=int(input("Enter number of elements to be added in first dictionary "))
dic1={}
for i in range(n1):
    key1=input("Enter key ")
    value1=input("Enter value ")
    dic1.update({key1:value1})
print("items in first dictionary ")
print(dic1)

n2=int(input("Enter number of elements to be added in second dictionary "))
dic2={}
for i in range(n2):
    key2=input("Enter key ")
    value2=input("Enter value ")
    dic2.update({key2:value2})
print("items in second dictionary ")
print(dic2)
dic1.update(dic2)
print("items after merge of first and second dictionary ")
print(dic1)


