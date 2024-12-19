n = int(input("Sonlarning sonini kiriting: "))
number = list(map(int,input("Sonlarni probel orqali kiriting: ").split()))

count = 0

for i in range(n-1):
    if number[i] < number[i+1]:
        count =+ 1

print(count)