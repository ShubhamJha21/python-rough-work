"""input n = 5
than take a boolean variable
print
*
**
***
****
***** if boolean is true
print
*****
****
***
**
*"""
i = 1
print("give the value of n ")
n = int(input())
print("select the value of boolean also")
b = int(input())
if b == 1:
  while(i<=n):
      print(i*"*",end = " \n")
      i = i+1
else:
    i=1
    while(1):
     while(i<=n):
               print(n*"*",end =" \n")
               n = n-1


#by yasir
"""print("How Many Row You Want To Print")
one = int(input())
print("Type 1 Or 0")
two = int(input())
new = bool(two)
if new == True:
   for i in range(1, one + 1):
       for j in range(1, i + 1):
           print("*", end=" ")
       print()
elif new == False:
   for i in range(one, 0, -1):
       for j in range(1, i + 1):
           print("*", end="")
       print()"""








