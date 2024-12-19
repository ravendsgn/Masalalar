n = int(input(" n Kiriting: "))
numbers = list(map(float, input("Probeldan sonlarni kiriting : ").split()))

def check_sawtooth(numbers):
    for i in range(1, len(numbers) - 1):
        if not ((numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]) or
                (numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1])):
            return i + 1  
    return 0

print(check_sawtooth(numbers))
