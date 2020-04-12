# import random
# # random_no = random.randint(1,6)
# # print(random_no)
# # random1 = random.random()*200
# # print(random1)
# list = ["sita","shruti","rahul","shubham","bholenath"]
# raise_fu = random.choice(list)
# print(raise_fu)

# import Platform
# x = Platform.system()
# print(x)


import random
characters = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
lenght = input('Enter Password lenght:')
lenght = int(lenght)
a  = ''
# for i in range (lenght):
for i in range(lenght):
         a = random.choice(characters)+a
print("Your Password is :" , a)