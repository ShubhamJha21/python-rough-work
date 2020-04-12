
Client_List={1:"harry",2:"shub",3:"sita"}
Lock_Retrive ={1:"exercise",2:"Diet"}
try:
 def getdate():
     """You can use getdate() to get current date and time"""
     import datetime
     return datetime.datetime.now()
 print("select client name")
 for key,value in Client_List.items():
    print("press",key,"for","client",value)
 key = int(input())
 print(Client_List[key],"press 1 to lock \n press 2 for retrieve")
 lo = int(input())
 if lo==1:
                 print("press 1 for Exercise \n press 2 for diet")
                 x = int(input())
                 if x==1:
                    k = "y"
                    print(Client_List[key]+" you lock"+ Lock_Retrive[1])
                    print("Enter Your " ,Lock_Retrive[1] , " Details")
                    while(k=="y"):
                     f = open(Client_List[key]+"-"+Lock_Retrive[1]+".txt","a")
                     print(getdate.__doc__)
                     a = f.write("[" + str(getdate()) + "]" +input()+"\n")
                     print(a)
                     print("add more y/n?")
                     k = input()
                     continue

                    f.close()


                 else :
                     k = "y"
                     print("you lock", Lock_Retrive[x])
                     print("Enter Your "+Lock_Retrive[x]+" Details")
                     while (k == "y"):
                         f = open(Client_List[key] + "-" + Lock_Retrive[2] + ".txt", "a")
                         a = f.write("[" + str(getdate()) + "]" + input()+"\n")
                         print(a)
                         print("add more y/n?")
                         k = input()
                         #continue

                         #f.close()
 elif lo == 2:
  print("which fie you want retrive?\n press 1 for exercise \n press 2 for Diet")
  x = int(input())
  s = open(Client_List[key]+"-"+Lock_Retrive[x]+".txt","rt")
  #content = s.readlines()
  for line in s:
   print(line)
  s.close()
 else:
     print("Invalid Input")

except Exception as e:
    print(e)






