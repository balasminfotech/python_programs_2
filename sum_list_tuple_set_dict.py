val=[1,2,3,4,5]
print(val)
print(type(val))
print("List the container using sum : ", sum(val))

val=(1,2,3,4,5)
print(val)
print(type(val))
print("Tuple the container using sum : ", sum(val))

val={1,2,3,4,5}
print(val)
print(type(val))
print("Set the container using sum : ", sum(val))

val={"a":1,"b":2,"c":3,"d":4,"e":5}
print(val)
print(type(val))
count=0
for i in val:
    count=count+val[i]

print("dict the container using sum : ", str(count))