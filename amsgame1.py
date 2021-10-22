# subtraction game

def euclid_gcd(a, b):
    while b:
        t = b
        b = a % b
        a = t
    return a


def calculate_min(n, d):
    g = d[0]
    if len(d) == 1:
        return g
    else:
        for i in range(1, n):
            g = euclid_gcd(g, d[i])
        return g


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        length_of_list = int(input())
        list_to_check = list(map(int, input().rstrip().split()))
        result.append(calculate_min(length_of_list, list_to_check))
    print(*result, sep='\n')
