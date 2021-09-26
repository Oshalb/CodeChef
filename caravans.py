# Max Speed of cars

result = []
for _ in range(int(input())):
    count = c = 0
    number_of_cars = n = int(input())
    speed_of_cars = ns = list(map(int, input().rstrip().split()))
    max_speed = m = float('inf')
    for i in ns:
        if i <= m:
            c += 1
            m = i
    result.append(c)

print(*result, sep='\n')
