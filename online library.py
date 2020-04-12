class Online_Library():
    def __init__(self,books,library_name):
        self.books = books
        self.libaryname = library_name
        self.user_data = {}
    def display_book(self):

             print(f"{self.books}")

    def lendbook(self,user,book):
        if book not in self.user_data.keys():
            self.user_data.update({book:user})
            print("update succefully: you can take ",book)

        else:
            print(f"book alredy had taken by {self.user_data[book]}")

    def addbook(self,book):
        self.books.append(book)
    def returnbook(self,book):
        self.user_data.pop(book)
        print("return successfully")

shubham_library = Online_Library(["python","c++","c","java","javascript"],"shubhamjha_library")
try:
 while 1:
     print("press following key to continue")
     print("(a) for book_display")
     print("(b) for book_lend")
     print("(c) for book_add")
     print("(d) for book_return")
     user_choise = input()
     if user_choise not in ["a","b","c","d"]:
         print("no match key found for  press 1 to quit or 2 to continue ")
         if user_choise == "1":
             exit()
         else:
             print("choose a valid key from " "a","b","c","d")
     else:
         if user_choise == "a":
             shubham_library.display_book()
         elif user_choise == "b":
             print("enter your name")
             user = input()
             print("enter book name")
             book = input()

             shubham_library.lendbook(user,book)
         elif user_choise == "c":
             print("enter book name to add in library")
             book = input()
             shubham_library.addbook(book)
         elif user_choise=="d":
             print("return book name")
             print("enter your book name")
             book = input()
             shubham_library.returnbook(book)

except Exception as e:
    print(e)

