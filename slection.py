n=int(input("specify the num :"))
lst=[]
print("enter ele")
for i in range(n):
        temp=int(input())
        lst.append(temp)

        print("ele of list are :")
        print(lst)

        i=0
        while i<n-1:
         j=j+1
        while j<n:
            if lst[j]<lst[i]:
                t=lst[j]
                lst[j]=lst[i]
                lst[i]=t

        j=j+1
i=i+1

print("ele of sorting is",lst)

