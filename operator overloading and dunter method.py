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