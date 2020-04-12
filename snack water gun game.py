import random
i = 0
v = 0
k =10
while(i < 10):
     print("no of chances left =",k)
     print("choose snack,water or gun any one\n",end = "")
     b = input()
     list = ["snack","water","gun"]
     a = random.choice(list)
     if b==a:
         print("game try")
     elif int(b=="snack")& int(a=="water"):
         print("you won")
         v = v + 1
     elif int(b == "water")  & int(a == "gun"):
         print("you won")
         v = v + 1
     elif int(b == "gun")  & int(a == "snack"):
         print("you won")
         v = v + 1
     else:
         print("you lose")
     k = k-1
     i = i +1
print("total winning =",v ,"total lossing =",10-v)
c = v
d = 10-v
if c>d:
    print(" Final result : you win")
else:
    print("Final result: you loss")



