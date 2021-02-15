str=input("Enter string ")
counts=dict()
words=str.split()
for i in words:
    if i in counts:
        counts[i]+=1
    else:
        counts[i]=1

print(counts)        
