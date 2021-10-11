# factors of a number
from math import sqrt

if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        number_to_check = n = int(input())
        s = int(sqrt(n))
        a = float('inf')
        for i in range(1, s+1):
            if n % i == 0:
                y = n // i
                a = min(a, y - i)
        result.append(a)
    print(*result, sep='\n')
