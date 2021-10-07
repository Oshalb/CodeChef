# comapare comninations
from itertools import combinations as ncr


def check_continous(a, n):
    c = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            c += 1
    return c


def check_pair(b, n):
    cb = [num for num in ncr(b, 2)]
    t = 0
    for i in cb:
        if i[0] > i[1]:
            t += 1
    return t


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        total_numbers = int(input())
        list_of_numbers = list(map(int, input().rstrip().split()))
        if total_numbers == 1:
            result.append("YES")
        else:
            if check_pair(list_of_numbers, total_numbers) == \
                    check_continous(list_of_numbers, total_numbers):
                result.append("YES")
            else:
                result.append("NO")
    print(*result, sep='\n')
