n=[5,10,15,2,4,6]
result=[]
ther=[]
for i in n:
    if i%5==0:
        result.append(i)
    else:
        ther.append(i)

print(result)
print(ther)
