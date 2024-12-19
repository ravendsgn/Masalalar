n = int(input("n kiriting: "))
numbers = list(map(float, input("Sonlarni kiriting: ").split()))

def reverse_power(numbers):
    n = len(numbers)
    return [numbers[i]**(n - i) for i in range(n)]

print(reverse_power(numbers))
