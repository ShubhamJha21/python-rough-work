# uses : class method is used for to change class instants
class Friends:
    no_of_friends = 8

    def __init__(self, aproffesion, agraduate, aage):
        self.proffession = aproffesion
        self.graduate = agraduate
        self.age = aage

    def func(self):
        return f"{self.proffession},{self.graduate},{self.age}"
    @classmethod
    def bbhua(cls, param):
        cls.no_of_friends = param
    # here we use class method as alternative to pass objest to class with out argument in class

    @classmethod
    def split_using_dash(cls,str):
        karam = str.split("-")
        return cls(karam[0],karam[1],karam[2])

karan = Friends.split_using_dash("student-yes-24")
print(karan.graduate)
print(karan.func())

# shubham = Friends("student", "yes", "23")
#
# shubham.bbhua(3999)t
# print(Friends.no_of_friends)
