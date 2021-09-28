# Check characters in a string

def count_jewels(s, t):
    c = 0
    for i in t:
        if i in s:
            c += 1
    return c


if __name__ == "__main__":
    result = []
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        string_of_jewels = str(input())
        string_of_rocks = str(input())
        result.append(count_jewels(string_of_jewels, string_of_rocks))

    print(*result, sep='\n')
