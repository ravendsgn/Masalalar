n = int(input(" n Kiriting: "))
numbers = list(map(float, input("Probeldan sonlarni kiriting : ").split()))

def sum_between_first_and_last_zeros(numbers):
    first_zero = numbers.index(0)
    last_zero = len(numbers) - 1 - numbers[::-1].index(0)
    return sum(numbers[first_zero + 1:last_zero])

print(sum_between_first_and_last_zeros(numbers))
