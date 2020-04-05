import os
def readException():
    try:
        sourceFilePath=os.path.abspath(r"FileExample\myfile.txt")
        print(">>>",sourceFilePath)
        f1=open(sourceFilePath)
    except IOError as a:
        print("Could not open file=",a)
print("Learning Exception Handling")
readException()
print("---End---")