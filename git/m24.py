n = int(input(" n Kiriting: "))
numbers = list(map(float, input("Probeldan sonlarni kiriting : ").split()))

def sum_between_last_two_zeros(numbers):
    nollar = [i for i, x in enumerate(numbers) if x == 0]
    if len(nollar) < 2:
        return "Ikta noldan kam!"
    return sum(numbers[nollar[-2] + 1:nollar[-1]])

print(sum_between_last_two_zeros(numbers))
