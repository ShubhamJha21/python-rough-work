#Exercise
"""hide a number in program n = 18
Enter the Number
guess it is bigger or smaller than that hidden no
tell : print no of guesses he took to finish
game over"""
"""list = [11,13,12,14,15,16,17,18,19,20]
count= 0
i = 0
p = 0
if list[i]<18:
   while(1):
     i = int(input())
     if i<18:
        print("no is smaller than desired no.")
        count = count + 1
     continue
   print("no is greater than desired no")
p = count
p = p+1
while(1):
 i = i-1
 if i==18:

    print("game over")
    print("no of guess",p)
 else: p = p + 1
 i = i-1
 if i == 18:
  print("game over")
  break
  print("no of guess", p)
else:
    print("print no bw 10 to 21")"""
"""Pinned by CodeWithHarry
Hamad Shigri
1 year ago"""
n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")

