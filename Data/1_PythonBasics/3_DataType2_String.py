#Break till 11.30
#Example for String data 
s = '012345'                #string s defined with value 012345 assigned to it
print ("Original string s = ", s)                     #012345
print ("0th index charater from string s = ",s[0])    #0
print ("Character at -ve index -1 = ", s[-1])         #5
print ("String from 1 to 4 index = ",s[1:4])          #123
print ("String after index 2 =",s[2:])                #2345
print ("String upto 4 index = ",s[:4])                #0123
#print ("character at 8 index = ",s[8])               #IndexError: string index out of range
print ("-----------------------------------------------------")

str1 ="Nilakantha"
print ("Original string str1  = ", str1)              #Nilakantha
size = len(str1)    #str1.len  not call like this
print ("length of str1 = ", len(str1))                #10
print ("-----------------------------------------------------")
str ="Welcome to datalitics. datalitics Pune"
print ("Original string str  = ", str)                #Welcome to datalitics. datalitics Pune
#count1 = str.count('datalitics',0,len(str))
count1 = str.count('datalitics',0,99)
#str.isalpha()
print ('Count of datalitics in str = ',count1)               #2
print ("-----------------------------------------------------")
print ("String formats in Python = ")
print ("one, %.2f, two" % 8 )                                   #one, 2, two
print ("%s two %s"         %(1,'three'))                        #1 two three
print ("Hello repeated 3 times using * operator = ", 'Hello'*3) #HelloHelloHello
print ("Checking existance of substring e in hello = ",  'e' in "hello")      #True
print ("String from -3 to -1 index = ",'hello'[-3:-1])                        #ll
print ("-----------------------------------------------------")
#strings are immutable
s ="Hello"   #some memory
print ("original s =", id(s))
s = s+ "world"   #a different memory
print ("Changed  s =", id(s))
print ("-----------------------------------------------------")
print (dir(s))   #return you a list  denoted by symbol [], list of all attributes and built in functions for passed
                 #object parameter - s

#print ("index of hello in Helloworld = ", s.index("xy"))#ValueError: substring not found
print ("index of hello in Helloworld = ", s.index("world"))
print ("-----------------------------------------------------")
#raw string
s1 = "c:\temp\new.txt"
print ("S1 = ",s1)
print ("-----------------------------------------")

s2 = "c:\\temp\\new.txt"   
print ("S2 = ",s2)              #c:\temp\new.txt
print ("-----------------------------------------")

s3 = r"c:\temp\new.txt"         #raw string    r   R in pattern matches - regular expression
print ("S3 = ",s3)              #c:\temp\new.txt
print ("-----------------------------------------")
#raw string to a variable
str_text = "c:\test\new.txt"
str_text = "%r"%str_text
print ("str text = ", str_text) #'c:\test\new.txt'
raw_text = str_text[1:-1]       #c:\test\new.txt
print ("raw text = ", raw_text)











