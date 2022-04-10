val1=int(input("Enter value 1"))
val2=int(input("Enter value 2"))
val3=int(input("Enter value 3"))
max1=max(val1,val2,val3)
min1=min(val1,val2,val3)

sum1=(val1+val2+val3)-(max1+min1)
print(min1,sum1,max1)