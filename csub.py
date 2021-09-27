# Count number of substring's

# 1 1
# 1 1
result = []
for _ in range(int(input())):
    length_of_string = n = int(input())
    string_to_check = s = str(input())
    count = c = s.count('1')
    r = (c * (c + 1)) // 2
    result.append(r)

print(*result, sep='\n')
