# Find number of trailing zeros of a factorial

def count_zeros(n):
    z = 5
    c = 0
    while n / z > 0:
        c += int(n / z)
        z *= 5
    return c


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        number_to_check = int(input())
        result = count_zeros(number_to_check)
        print(result)
