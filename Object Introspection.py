class Mobiephones():
     def __init__(self):
         self.brand = ["mi","nokiya","lenovo"]
         self.battery_capacity =["3000mhz","4000mhz","6000mhz"]

     def rint_details(self):
         return f"mobile brands {self.brand} have {self.battery_capacity} battery capacity"
     def ispe(self,str,classstr):
         self.object = str
         namre =self.class1 =  classstr
         import inspect
         return f"All members of mobiles object are \n {inspect.getmembers(self.object)} \n is it a class if yes than return trues else false\n {inspect.isclass(self.object)}\n all members of main class Mobile_phone are \n {inspect.getmembers(namre)}  "
mobiles = Mobiephones()
print(mobiles.rint_details())
print(mobiles.ispe("mobiles","Mobilephones"))



