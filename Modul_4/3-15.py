work_experience = int(input("Введите свой стаж полных лет: "))

if  1 < work_experience <= 5 : 
    developer_type = "Middle"
elif work_experience <= 1 :
    developer_type = "Junior"
else:
    developer_type = "Senior"
print(developer_type)

