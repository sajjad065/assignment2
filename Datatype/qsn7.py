total=int(input(" How many  words do you want to insert in the list "))
list1=[]
length=0
for i in range(total):
                  num=input("Enter words ")
                  list1.append(num)
for j in list1:
   if(length<len(j)):
      length=len(j)
print("the length of the longest word is " +str(length))
      
