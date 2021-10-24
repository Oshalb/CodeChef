# distinct number list

if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        length_of_list = n = int(input())
        list_to_check = a = list(map(int, input().rstrip().split()))
        result.append((n * (n-1)) // 2)
    print(*result, sep='\n')
