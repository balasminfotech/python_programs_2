string ='123ayu456'
newstring2 =""
r=[]
for a in string:
    if (a.isnumeric()) == True:
        r.append(a)
    else:
        newstring2+= a

print(''.join(r), "total no is {}".format(len(r)))
print(newstring2, " total leters are {}".format(len(newstring2)))