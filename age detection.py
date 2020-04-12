print("Enter your Age")
age = input()
if int(age) < 18:
    print("you are not eligible for driving license")
elif int(age) == 18:
    print("some driving test require")
else :
    print("you can make your driving license")