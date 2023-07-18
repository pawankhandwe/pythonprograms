fp=open("D:\my pc\pawan\gfg.txt","x")

print(fp)

if fp:
    print("file created sucessfully !!!")

fp=open("D:\my pc\pawan\gfg.txt","w")
fp.write("DATA  IS SUCCESSFULLY WRITTEN IN FILE !!!")
fp.close()
print("data written sucessfully ")

fp=open("D:\my pc\pawan\gfg.txt","a")
fp.write("new content is appended sucessfully to file !!!!!")
fp.close()
print("data appended sucessfully")

print("reading data from file")
fp=open("D:\my pc\pawan\gfg.txt","r")

for i in fp:
    print(i)

print("DATA READING FROM FILE IS SUCESSFULL !!!!")
fp.close()
