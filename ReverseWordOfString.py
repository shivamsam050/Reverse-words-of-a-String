str1= raw_input("enter The String")
str1 = str1[::-1]
l = []
k=0
for i in range(len(str1)):
    if(str1[i]== " "):
        str2= str1[k:i]
        str2= str2[::-1]
        l.append(str2)
        k=i
str2= str1[k:len(str1)]
str2= str2[::-1]
l.append(str2)
tuple1 =tuple(l)
for i in tuple1:
    print(i),
else:
    print        
        
