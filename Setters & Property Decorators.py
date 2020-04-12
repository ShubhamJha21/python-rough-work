class employee():
    def __init__(self,fname,sname):
        self.fname =fname
        self.sname = sname
        # self.email = f"{self.fname}.{sname}@gmail.com"
    def explain(self):
        return f"{self.fname}.{self.sname}@gmail.com"
    @property
    def email(self):
        if str(self.fname)=="none" or self.sname == "none":
            return ("email not valid")
        else:
          return (f"{self.fname}.{self.sname}@gmail.com")

    @email.setter
    def email(self, string):
        name  = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.sname = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = "none"
        self.sname = "none"


shubham_jha = employee("shubham","jha")
sita_ram_yadav: employee = employee("sita","ram")
print(sita_ram_yadav.email)
sita_ram_yadav.fname = "ashoka"
print(sita_ram_yadav.email)
sita_ram_yadav.email = "sitaram.jha@gmail.com"
sita_ram_yadav.email = "sunil.mishra@gmail.com"
print(sita_ram_yadav.email)
print(sita_ram_yadav.fname)
print(sita_ram_yadav.sname)
# del sita_ram_yadav.email
print(sita_ram_yadav.email)
