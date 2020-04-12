# list = ["aalu", "bhindi", "gobhi", "kaddu"]
# i = 1
# for item in list:
#     if i % 2 != 0:
#       print(item)
#     i=i+1
# use for list to write in form of dict (key,value)

list = ["aalu", "bhindi", "gobhi", "kaddu"]
for index,item in enumerate(list):
     if index%2==0:
          #use f string
         print(f"jarvis buy {item}")