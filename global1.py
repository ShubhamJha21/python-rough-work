# globel variable l = 10
"""l = 10
def shubham(n):
     l = 12 #local variable
     print(n,"i am shubham",l)
shubham("great learner")
print(l)"""
# Global key
a =89
def jha():
    a =10
    def jhaji():
        global a
        a=20
    # print("before calling jhaji",a)
    jhaji()
    print("after calling jhaji",a)
jha()
print(a)