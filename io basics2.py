
"""f = open("shubham.txt", "rt")
content =f.read(12345)
print("01",content,end=" ")
content =f.read(1234)
print("\n02",content,end=" ")
f.close()"""

#1)))) print charater by character program using for
"""f=open("shubham.txt")
content=f.read( )
for line in content:
 print(line)
 f.close()
 """

#2)))print all line in text file we use readlines() function or for loop function
# for reading single line we use readline() function and
"""f = open("shubham.txt")
for line in f:
 print(line,end = " ")
 f.close()"""

# 3))) to open lines one by one
"""f = open("shubham.txt")
x = f.readline()
print(x,end = "")
print(x,end = "")
print(x,end = "")"""

#4)))to write the file
"""f = open("jha.txt","w" )
f.write("shubham jha ko abhi bahut kuch sikhna hai ")
f.close()"""

#5))) to append the new line in txt file we use (a for append)
"""f = open("jha.txt","a")
a= (f.write("shubham faltu bakchodi karke apna samay barbad nahi karta\n"))
f.close()"""

# how to read and write text file
#for this we use r+ io method
s = open("jha.txt","r+")
content = s.read()
print(content)
s.write("shubham is a humble guy\n")
s.close()





