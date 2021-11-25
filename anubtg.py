# Sort and Pair

def find_total(a, n):
    b = sorted(a, reverse=True)
    k = 0
    for i in range(n):
        if i%4 < 2:
            k += b[i]
    return k


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        length_of_list = int(input())
        prices_to_check = list(map(int, input().rstrip().split()))
        result.append(find_total(prices_to_check, length_of_list))
    print(*result, sep='\n')
