# subsequence

if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        length_of_list = int(input())
        list_to_check = a = set(map(int, input().rstrip().split()))
        result.append(len(a))
    print(*result, sep='\n')
