def func19(numbers):
    result = []

    for i in range(1,len(numbers)):
        if numbers[i] < numbers[i-1]:
            result.append(i)

    return result, len(result)

n = 6 
numbers = [10, 5, 6, 3, 8, 2]

small, count =func19(numbers)

print("chap tarafdagi sonlardan kichik sonlar: ", small)
print("shunday sonlarni soni: ", count)