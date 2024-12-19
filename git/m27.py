n = int(input("n kiriting: "))
numbers = list(map(float, input("Sonlarni kiriting: ").split())) 

def power_by_index(numbers):
    return [x**(i + 1) for i, x in enumerate(numbers)]

print(power_by_index(numbers))