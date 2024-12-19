n, k = map(int, input(" n va k ni kiriting: ").split()) 
numbers = list(map(float, input("Sonlarni kiriting: ").split())) 

def power_all(numbers, k):
    return [x**k for x in numbers]

print(power_all(numbers, k))
