#Example for basic data type values
x=100                                       #x variable declared with ineger value assigned
z=3.45                                      #z variable declared with fractional value assigned
y='Hello'                                   #y variable declared with string literal value assigned
print ('int x value = ',x)                  # int x value  = 100
print ('string y value = ',y)               # string y value = Hello
print ("-------------------------------------------------")

if z==3.45 or y=='Hello':                   #if loop construct to compare values in or condition
    print ("In if loop block")
    x =x+1                                  #here indentation is must for if loop code block
    y=y+' World'                            # + is concatenation operator
else:print ("In else block")      
print ("-------------------------------------------------")
print ("int value of z = 3.45 is = ", int(z))         #int value of z = 3.45 is =  3
print ("float value of x = 101 is = ", float(x))      #float value of x= 101 is =  101.0
print ("-------------------------------------------------")
print ("Triple quoted string = ", """a'b"c""" )       #a'b"c
print ("Double quoted string = ", "Kinght's")         #Kinght's
print ("Single quoted string = ", 'Kinght"s' )        #Kinght"s
print ("Using backslash escape character : AAA\"BBBBB")#Using backslash escape character : AAA"BBBBB
print ("-------------------------------------------------")
#print (x+"AAAA")                                     #concatenation if int and string is not poosible   TypeError: unsupported operand type(s) for +: 'int' and 'str'
print ("""a
        b
            c""")
#raw string
print ('c\temp\new.txt')                              #\t and \n escape charaters are resolved as tab and new line character
print (r'c\temp\new.txt')                             #r for raw string    R
str1= (r'c\temp\new.txt')
print ("str1 =",str1)
#print (r'c\10\')         #Syntax error ending \ not allowed in any string value 

"""Doc string
This is Data types in 
Python
Interesting
"""






























"""
#1,2,3,4    Tuple   
(1,2,3,4)


[1,2,3,4,"one", 3.14]  List
"""




























    
