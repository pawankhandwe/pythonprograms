lst1=[2,3,5,7,8]
lst2=[12,15,20]

print("print"+str(lst2[1]))
print("2 to 4 ele"+str(lst2[2:4]))

lst2[0]=16
print("update "+str(lst2))
del lst1[0]
print("deleted"+str(lst1))
lst3=[]
lst3=lst1+lst2

print(lst3)
l=len(lst3)
print(str(l))