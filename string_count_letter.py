st="The quick brown fox jumps over the lazy dog."
result=0
for i in st:
    if i=="o":
        result +=1
print("This letter appears {} times".format(result))