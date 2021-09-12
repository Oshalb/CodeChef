# Ciel and A-B Problem

def wrongsub(a, b):
    c = a - b
    if c % 10 == 9:
        c -= 1
    else:
        c += 1
    return c


if __name__ == "__main__":
    first_number, second_number = map(int, input().rstrip().split())
    result = wrongsub(first_number, second_number)
    print(result)
