def F(n, k, left, right):
    if len(k) == 2*n:
        h.append(k)
        return 
    if left < n:
        F(n, k + '(', left + 1, right)
    if right < left:
        F(n, k + ')', left, right + 1)
    return h
n = int(input())
h = []
print(F(n, '', 0, 0))