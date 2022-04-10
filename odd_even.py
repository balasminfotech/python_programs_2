values=int(input("Enter number to find odd or even : "))
mod=values % 2
if mod>0:
    print("the number {} is odd".format(values))
else:
     print("the number {} is even".format(values))