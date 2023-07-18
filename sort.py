print("enter ele")
n=int(input())
lst=[]
print("enter element")
for i in range(n):
 temp=int(input())
 lst.append(temp)

print("element of list are :")
print(lst)

lst.sort()
print(" sorted ele ")
print(lst)