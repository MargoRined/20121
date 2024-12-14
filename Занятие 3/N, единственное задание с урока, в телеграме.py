n1 = int(input())
n = [int(input()) for i in range(n1)]
b = set()
c = int(input())
g = 0
v = set()
v1 = set()
v2 = set()
for i in range(len(n)-3):
    for j in range(i+1, len(n)-2):
        for k in range(j+1, len(n)-1):
            for h in range(k+1, len(n)):
                b.add(n[i] + n[j] + n[k] + n[h])
                if (n[i] != n[j]) and (n[i] != n[k]) and (n[i] != n[h]) and (n[k] != n[j]) and (n[h] != n[j]) and (n[k] != n[h]):
                    b.add(n[i] + n[j] + n[k] + n[h])
b1 = list(b)
for u in b1:
    if c == u:
        g += c
    elif (c - u == 1) or (c - u == -1):
        v.add(u)
    elif (c - u == 2) or (c - u == -2):
        v1.add(u)
    elif (c - u == 3) or (c - u == -3):
        v2.add(u)
if g != 0:
    print(g)
elif (g == 0) and (len(v) > 0):
    print(min(v))
elif (len(v) == 0) and (len(v1) > 0) and (g == 0):
    print(min(v1))
elif (g == 0) and (len(v) == 0) and (len(v1) == 0) and (len(v2) > 0):
    print(min(v2))