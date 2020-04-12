class Friends():
    no_of_Friends = 8
    def __init__(self, aproffesion, agraduate, aage):
        self.profession = aproffesion
        self.graduate = agraduate
        self.age = aage
    def fun(self):
        return(f"my profession is {self.profession},what about graduation {self.graduate},my age is {self.age}")


shubham = Friends("STUDENT","YES","23")
sita = Friends("STUDENT","YES","22")
print(sita.fun())
print(shubham.profession)
print(Friends("STUDENT","YES","23"))