n = int(input(" n Kiriting: "))
numbers = list(map(float, input("Probeldan sonlarni kiriting : ").split()))

def check_descending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            return i + 1
    return 0

print(check_descending(numbers))
