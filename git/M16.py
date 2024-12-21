def func15(n,k):
    
    for i in range(len(n)-1,-1,-1):
        if n[i] > k:
            return i + 1
    return 0

n = [2, 7, 1, 13, 14,1, 0]
k = 6
result = func15(n, k)
print(result)