def func14(n,k):
    count = 0
    for i in n:
        if i > k:
            count += 1
    return count
n = [15, 8, 23, 7, 0]
k = 10
result = func14(n,k)
print(result)