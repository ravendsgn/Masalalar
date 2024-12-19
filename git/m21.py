n = int(input("Sonlarning sonini kiriting: "))
number = list(map(int,input("Sonlarni probel orqali kiriting: ").split()))

is_increasing = True

for i in range(1, n):
    if number[i] <= number[i - 1]:
        is_increasing = False
        break

if is_increasing:
    print("true")
else:
    print("false")
