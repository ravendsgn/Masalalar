n, k = map(int, input(" n va k kiriting: ").split())  # Пример: 6 2
numbers = [list(map(int, input().split())) for _ in range(k)]  # Пример: две строки: 1 2 3 и 4 5 6

def sum_all_groups(groups):
    return sum(sum(group) for group in groups)

print(sum_all_groups(numbers))
