vowels='aeiou'
str='aaiij'
cnt=0
lst={}
for i in range(len(str)):
    for char in vowels:
        if str[i]==char:
            if char not in lst:
                cnt =1
                lst[char]=cnt
            
            lst[char]=cnt
            cnt +=1
        
print(lst)

# if str in vowels:
#     print("vowels present in "+str)
# else:
#     print("vowels  not found  for "+str)

# ls=[]
# for char in vowels:
#     lst.append(char)

# apn=0
# for i in range(len(str)):
    # if str[i] in vowels:
    #     apn +=1
# print("total no of vowels present is : ", int(apn))

