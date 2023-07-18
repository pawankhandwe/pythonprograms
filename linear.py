print("enter in list")
n=int(input())
lst=[]

print("element of list")
for i in range(n):
    temp=int(input())
    lst.append(temp)
    
print("element of list",lst)
print("enter search ele")
x=int(input())

pos=-1
for i in range(n):
    if lst[i]==x:
        pos=i
        break

if pos!=-1:
    print("ele at index"+str(pos))
else:
   print("unsucess")
   
