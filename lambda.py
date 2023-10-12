# x = lambda a,b,c : a+b+c
# print(x(5,2,1))

# l1 = [12,34,5,6,8]
# l2=[]
# for i in l1:
#     t = lambda a : a+1
#     l2.append(t(i))
# print(l2)


# filters
# x1 = [12,12,3,4,56,19,32,45,65,18]

# def myfunc(x):
#     if x < 18:
#         return False
#     else:
#         return True
# adults = filter(myfunc,x1)
# print(list(adults))

# map()

# def calculateadd(n):
#     return n+n
# numbers = (1,2,3,4)
# result = map(calculateadd,numbers)
# print(list(result))

# reduce()
# from functools import reduce
# d = reduce(lambda a,b:a+b,[12,12,13,15,16])
# print(d)

def simplegenerator():
    yield 1
    yield 2
    yield 3
x = simplegenerator()
print(x.__next__())
print(x.__next__())
print(x.__next__())