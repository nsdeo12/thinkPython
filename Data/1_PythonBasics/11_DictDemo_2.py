"""Dictionary Def  key:value   mutable
key : immutable - int float str tuple   unique keys
value : anything - int float str tuple  list  dict set
"""
emp ={'1a':['ABC',25,25000]}
colors = {'red':255, 'blue':100, 'yellow':150, 'red':11}
print ("Colors dict = ", colors)  #unordered

print ("Value of red  =", colors['red'])   # 255

colors['yellow'] = 99
colors['magenta'] = 55
print ("Updated Colors  dict = ", colors)  #unordered
k = colors.keys()   
v = colors.values() 
print ("Keys = ", k , "type of k = ", type (k))#dict_keys(['red', 'blue', 'yellow', 'magenta'])  tyep of k =  <class 'dict_keys'>
print ("Values = ", v)#dict_values([11, 100, 99, 55])
print ("red exists ? = ", 'red' in colors)   #True
print ("Colors pairs = \n", colors.items()) #[('blue', 100), ('magenta', 55), ('yellow', 99), ('red', 11)]
l1 = list(k)
l1.sort()
print("Sorted list of keys = ",l1)
for i in l1:
    print ("Key = ",i, "Value = ", colors[i])
    colors[i]+=10

print ("------------------------------------------------")
for i in colors:
    print ("Key = ",i, "Value = ", colors[i])
#dict.clear
print(colors['BLACK'])   #KeyError: 'BLACK'


















    
