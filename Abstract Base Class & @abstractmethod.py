from abc import ABC,abstractmethod
class shap(ABC):
    @abstractmethod
    def print_statemrnt(self):
        return 0
class rectangle(shap):
    def __init__(self):
        self.no1 = 6
        self.no2 = 5
    def print_statemrnt(self):
       print(self.no1*self.no2)
abd = rectangle()
(abd.print_statemrnt())

