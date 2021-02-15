
s=input(" Enter String ")
count={}
for x in s:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1

print(count)
        
