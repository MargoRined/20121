list1 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25]
list2 = [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
c = set(list1) & set(list2)
print(len(c))
print(len(list1) + len(list2) - len(c)*2)
print(len(list1) - len(c))
print(len(list2) - len(c))