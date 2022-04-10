def strcheck(str):
    if len(str)>=2 and str[:2]=="Is":
        return str
    return "Is"+str
print(strcheck("Iss"))


def strcheck1(str,n):
    icnt=""
    for i in range(n):
        icnt=icnt+str
    return icnt
print(strcheck1("abc",2))

print("abc"*2)
