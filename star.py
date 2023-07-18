print("specify the order of pyramid")
r=int(input())

for i in range(r):
    strout=""
    for j in range(r):
        if j<=i:
            strout=strout+"*"+" "
           
    print(strout)            