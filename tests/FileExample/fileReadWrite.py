import os
# filePath=os.path.join(os.getcwd(),"FileExample")
sourceFilePath=os.path.abspath(r"FileExample\myfile.txt")
destFilePath=os.path.abspath(r"FileExample\destination.txt")
print(">>>",sourceFilePath)
f1=open(sourceFilePath,"r")
f2=open(destFilePath,"w")
while True:
    str=f1.readline()
    if str:
        print(">>",str)
        f2.write(str)
    else:
        print("Nothing in the file")
        break
f1.close()
f2.close()
    