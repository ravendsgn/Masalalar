def func15(n,k):
    count = 0
    for i,y in enumerate(n):
        if y > k:
            return i + 1
    return 0

n = [1, 5, 7, 3, 0]
k = 6
result = func15(n, k)
print(result) 
        
