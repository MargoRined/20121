k = [['name1surname1', 12345], ['name2surname2'], ['name3surname3', 12354], ['name4surname4', 12435]]
def santa_users(t):
    d = {}
    for i in t:
        if len(i) == 2:
            for x in range(len(i) - 1):
                d.update({(i[x]) : i[x+1]})
        else:
            for x in range(len(i)):
                d.update({(i[x]) : None})
    print(d)
santa_users(k)