def func18(n):

    w =[]
    for i in n:
        if n.count(i) == 1:
            w.append(i)
    return w
n = [1, 2, 2, 2, 3, 4, 4, 5]
result = func18(n)
print(result)