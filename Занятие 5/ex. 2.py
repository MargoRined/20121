from itertools import combinations 
list1 = ['a', 'b', 'c', 'd', 'd']
def F(a):
    g = []
    for r in range(1, len(set(list1)) + 1):
        for i in combinations(set(list1), r):
            g.append(set(i))
    return g
h = F(set(list1))
print(len(h))
   