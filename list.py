# lava = [12,2.9,"reddy",True]
# print(lava)
# print(type(lava))

# lava1 = list([1,2,5.9])
# print(lava1)/

# lava = [2.8,8.9,9.0,87,1,2,3,45]
# print(lava[7])
# print(lava[-1])

# slicing
# start:stop:slicing

# james_bond = [7,8,9,3,34,64,"true"]
# print(james_bond[0:5])
# print(james_bond[0:5:2])
# james_bond[0]="lava"
# print(james_bond)


# variable methods

lava = [1,2,3,4,56,67,89,90,23,45,98,98,98]
# lava.append(123)
# lava.extend([143])
# print(lava.index(98))
# print(len(lava))
# print(lava.count(98))
# print(lava[-1])
# print(lava)
# lava.insert(0,"lava")
# print(lava)
# lava.pop(8)
# print(lava)
# lava.remove(67)
# print(lava)77
# lava.reverse()
# print(lava)
# lava.sort()
# print(lava)
# lava.sort(reverse=True)
# print(lava)

# list=[x ** 2 for x in [1,2,3,4,5]]
# print(list)

# list1 = ["even" if i % 2 == 0 else "odd" for i in range(10)]
# print(list1)/

s = [1,2,2,2,2,2,2,3,4,5,6,7,2,8,2,92,10,2,210,2,98]
n=[]
for i in s:
    print(i)
    if i == 2:
        s.remove(2)
    else:
        n.append(i)
print(n)

