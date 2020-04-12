class electronic():

    voltage_supply = "5v"
    equipments = ["mobile charger","5 v adapter"]

    def blue(self):
        return("Boat_Bluetooth_speaker needed",self.voltage_supply+"supply and can charge using"+str(self.equipments))

class pocket_gadgets(electronic):
     var = "helpfull to track your fitness"
     def function(self):
       return (f" fitness tracker is {self.var} take ,{self.voltage_supply} supply and can charge using {self.equipments}")

class phone(pocket_gadgets):
    var2 = "can connect with these  elcetronic devices"
    def function2(self):
        return (f"Mi phone {self.var2}. it can also charge using dc ({self.voltage_supply} supply) and can charge with the help of  {self.equipments} and {self.var}")

Boat_Bluetooth_speaker = electronic()
Fitness_Tracker = pocket_gadgets()
Xiomi_MI = phone()

print(Boat_Bluetooth_speaker.blue())
print(Fitness_Tracker.function())
print(Xiomi_MI.function2())





