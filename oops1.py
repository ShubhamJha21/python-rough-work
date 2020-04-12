class Friends:
    no_of_Friends = 8
    pass
shubham = Friends()
sita = Friends()
shubham.profession = "student"
shubham.graduate = "yes"
shubham.age = 21
sita.profession = "student"
sita.graduate = "yes"
sita.age = 21
print(shubham.age,sita.profession,shubham.no_of_Friends,sita.no_of_Friends,Friends.no_of_Friends)
shubham.no_of_Friends = 9
print(shubham.__dict__)
print(Friends.__dict__)
Friends.no_of_Friends=10
print(sita.no_of_Friends)
