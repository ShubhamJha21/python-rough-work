def fun(normal,*args,**qwargs):
    print("these boys are in nbh")
    for item in args:
        print(item)
    print("\ntheir professions are\n")
    for key,values in qwargs.items():
        print(f"{key} has {values} profession")
list = ["rahul","ameya","aditya","shubham"]
dict = {"rahul":"intel","amey":"pmrf","aditya":"jp morgan","shubham":"programmer"}
normal ="these boys are in nbh boys hostel"
fun(normal,*list,**dict)
