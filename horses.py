# Minimum difference two numbers in a list

result = []
for _ in range(int(input())):
    number_of_horses = int(input())
    level_of_skill = list(map(int, input().rstrip().split()))
    ls = sorted(level_of_skill, reverse=True)
    min_diff = float('inf')
    for i in range(number_of_horses-1):
        m = ls[i] - ls[i+1]
        if m < min_diff:
            min_diff = m
    result.append(min_diff)

print(*result, sep='\n')
