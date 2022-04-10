# def concatenate_list_data(list):
#     result= ''
#     for element in list:
#         result += str(element)
#     return result

# print(concatenate_list_data([1, 5, 12, 2]))
val=[1,5,12,2]
result=''
for i in val:
    result +=str(i)
print(result)

val=["red","white","black"]
result=''
for i in val:
    result +="-"+i
print(result[1:])

list_of_colors = ['Red', 'White', 'Black']  
colors = '-'.join(list_of_colors)
# print()
print("All Colors: "+colors)
# print()
