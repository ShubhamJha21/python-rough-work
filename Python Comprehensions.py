# list comprehensions
# set comprehension
# generator comprehension
                                      # list comprehens
# lst = [i for i in range(10,100) if i%10==0]
# print(lst)
# set comprenhention
# lst ={i for i in range(10,100)}
# print(lst)
# lst =[name for name in ["shubham","shubham","shubham","sita"]]
# print(lst)


                                     # set comprenhention
# lst ={name for name in ["shubham","shubham","shubham","sita"]}
# print(lst)


# dress_code = {i:f"dress{i}" for i in range(1,101)}
# dress_code1 = {value:key for key,value in dress_code.items()}
# print(dress_code1)
#                                   get function comprenhention
# list =(i for i in range(2,20) if i%2==0)
# print(list.__next__())
# print(list.__next__())
# print(list.__next__())
# print(list.__next__())
# print(list.__next__())
# print(list.__next__())
# print(list.__next__())
# print(list.__next__())
# print(list.__next__())
class main():
    def __init__(self):
        print("how many items you want yo insert in this list")
        self.no_of_items = int(input())
        self.list =[]
        print("ok enter your items")
        for i in range(self.no_of_items):
            self.list.append(input())
        print(self.list)

    def fun(self):
        while 1:
            print("to write your program in list or set comprehension press 'a' for list comp. and 'b' for set and c for dictionary comprehention ")
            m = input()
            if m=="a":
                print("comprehension using list is ")
                list = [i for i in self.list]
                print(list)
            elif m=="b":
                print("comprehension using set is")
                list = {list for list in self.list}
                print(list)
            elif m=="c":
                print("comprehension using dict is")
                list = {i:f"{self.list[i]}" for i in  range(self.no_of_items)}
                print(list)
            elif m == "d":
                exit()
            else:
                print("you  enter wrong input")

no_of_items = main()
no_of_items.fun()


