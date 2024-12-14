s = str(input())
d = ''
h = 0
k = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
for i in range(len(s)-1):
    if s[i] in k:
        d += s[i]
    if (s[i] == ' ') and (s[i+1] == ' '):
        h += 1
        if h == 1:
            d += ' '
    if (s[i] == ' ') and (s[i+1] != ' '):
        d += ' '
d += s[-1]
h = d.split()
h.reverse()
r = " ".join(h)
print(r.capitalize())