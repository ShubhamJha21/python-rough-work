# def listSorting(list):
#     return list[0]
# list = [[1, 2], [0, 1], [3, 2]]
# list.sort(key=listSorting)
# print(list)
# list = [[0,2],[1,1],[8,9],[9,8]]
# list.sort(key = lambda list:list[1])
# print(list)
# #2)) by using lambda
# minus = lambda a,b:a-b
# print(minus(5,4))
# #1)) subtraction
# def minus(a,b):
#      return a-b
# a = int(input())
# b = int(input())
# print(minus(a,b))
#1)) subtraction
# def minus(a,b):
#      return a-b
# a = int(input())
# b = int(input())
# print(minus(a,b)


# #2)) by using lambda
# minus = lambda a,b:a-b
#  print(minus(5,4))


#3)) Sorting
def listSorting(list):
       return list[0]
list = [[1,2],[0,1],[3,2]]
list.sort(key = listSorting)
print(list)
""" Output = [0,1],[1,2],[3,2] """


#4))Sorting Lambda
list = [[0,2],[1,1],[8,9],[9,8]]
list.sort(key = lambda list:list[1])
print(list)
""" Output = [[1, 1], [0, 2], [9, 8], [8, 9]]"""
