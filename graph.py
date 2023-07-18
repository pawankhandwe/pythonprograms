import matplotlib.pyplot as plt

n=int(input("specify the number of points :"))
print("specify th X value of each point :")

xlst=[]
for i in range(n):
    temp=int(input())
    xlst.append(temp)

    ylst=[]
    for i in xlst:
        if i%2==0:
            temp=i/2
            ylst.append(temp)

print("points to plot are :")
i=0
l=len(xlst)

while i<l:
    print("("+str(xlst[i])+","+str(ylst[i])+")") 
    i=i+1


plt.xlabel("independent variable -X")
plt.ylabel("dependent varaibale - Y")

plt.plot(xlst,ylst)
plt.show()

