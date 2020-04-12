
"""print("Track Your Health Routine")
ClientList = ["Shubham","Sitaram","Naved"]
print("Enter Your User No. that start from 0")
UserNo = int(input())
print("what you want to lock? Exercise or Diet")
print("press 1 for Exercise or press 2 for dite")
a = int(input())
while(1):
 if a==1:


        import datetime
        b= datetime.datetime.now()
        print(datetime.datetime.now())
        print("which Exercise you perform")
        d = input()
        print(ClientList[UserNo],b,d)
else:
  import datetime
b= datetime.datetime.now()
print(datetime.datetime.now())
print("what you eat today")
c = input()
print(ClientList[UserNo], b,c)"""
# Health Management System

client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
lock_list = {1: "Exercise", 2: "Diet"}
def getdate():
    import datetime
    return datetime.datetime.now()
try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())

    print("Selected Client : ", client_list[client_name], "\n", end="")

    print("Press 1 for Lock")
    print("Press 2 for Retrieve")
    op = int(input())

    if op == 1:
        for key, value in lock_list.items():
            print("Press", key, "to lock", value, "\n", end="")
        lock_name = int(input())
        print("Selected Job : ", lock_list[lock_name])
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
        k = 'y'
        while (k != "n"):
            print("Enter", lock_list[lock_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()
    elif op == 2:
        for key, value in lock_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        lock_name = int(input())
        print(client_list[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as e:
    print(e)






