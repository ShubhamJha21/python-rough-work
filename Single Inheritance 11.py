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

    # @classmethod
    # def split_using_dash(cls,str):
    #     karam = str.split("-")
    #     return cls(karam[0],karam[1],karam[2])
class job(Friends):
    def __init__(self,aproffesion, agraduate, aage,language):
        self.proffession=aproffesion
        self.graduate=agraduate
        self.age= aage
        self.language=language

    def printprog(self):
        print(f"the jobs of {self.proffession },is he graduate?={self. graduate},his age is {self.age},he knowes {self.language}")

harry = job("programmer","344","455",["python","c++"])
print(harry.func())
harry.printprog()
