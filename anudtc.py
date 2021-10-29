# parts of a circle

def check_circle(n):
    c = "a b c"
    if 360 % n == 0:
        c = c.replace('a', 'y')
    else:
        c = c.replace('a', 'n')
    if n <= 360:
        c = c.replace('b', 'y')
    else:
        c = c.replace('b', 'n')
    if (n * (n + 1)) / 2 <= 360:
        c = c.replace('c', 'y')
    else:
        c = c.replace('c', 'n')
    return c


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        number_to_check = int(input())
        result.append(check_circle(number_to_check))
    print(*result, sep='\n')
