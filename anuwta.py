# Total difference

# 0 1 2 3
# 0 0 0 0
# 0 0 0 1 - 3
# 1 0 0 1 - 3
# 1 0 1 1 - 2
# 1 1 1 1 - 1

if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        number_to_check = n = int(input())
        r = ((n * (n+1)) // 2) + n
        result.append(r)
    print(*result, sep='\n')
