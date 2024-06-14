# profile1 = {
#     "Name": "Kenny",
#     "Age": 27
# }

# profile2 = {
#     "Name": "Neutron",
#     "Age": 20
# }


# profile3 = {
#     "Name": "Walter",
#     "Age": 24,
#     "Contacts": [profile1, profile2]
# }


# # for value in profile3.values():
# #     print(value)

# for contact in profile3["Contacts"]:
#     for value in contact.values():
#         print(value)


class  Human:
    def __init__(self, name, sex, age, hobby):
        self.name = name
        self.sex = sex
        self.age = age
        self.hobby = hobby




person1= Human("Kenny Neutron", "male", 27, "Programming")
person2= Human("Naruto Uzumaki", "male", 29, "Ninjutsu")
person3= Human("Sakura Haruno", "female", 30, "Nothing")

lperson= [person1, person2, person3]


temp_var=1
for person in lperson:
    if (person.sex == "male"):
        print(f"Person{temp_var} is {person.name}, he is {person.age} years old, and his hobby is {person.hobby}")
    elif (person.sex == "female"):
        print(f"Person{temp_var} is {person.name}, she is {person.age} years old, and her hobby is {person.hobby}")
    temp_var+=1