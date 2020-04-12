# import time
# def searcher():
#     book="this is shubham jha under construction"
#     time.sleep(4)
#     while 1:
#         if text := (yield) in book:
#             print("text is in book")
#         else:
#             print("text is not in book")
# search = searcher()
# next(search)
# search.send("shubham")
# k = input("enter any key")
# search.send("this is")
# k = input("enter any key")
# search.send("sita")
# k = input("enter any key")
# search.send("razm")
# k = input("enter any key")
# search.send("construction")
import time

def search_key_word():
    f = open("file1.txt")
    g = open("file2.txt")
    time.sleep(4)
    while 1:
        text = (yield)
        found =''

        for line in f:
            if text in line:
                found = True
                break
        if found==True:
           print(" text found in file1")
        else:
            for line in g:
               if text in line:
                   found = True
                   break
        if found == True:
           print(" text found in file2")
        else:
            print("file not found")


search =search_key_word()
next(search)
print("Search your word")
search.send(input())







