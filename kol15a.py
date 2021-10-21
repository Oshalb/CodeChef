# string to num sum

def find_sum(s):
    c = 0
    dig = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    for i in s:
        if i in dig:
            c += int(i)
    return c


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        string_to_check = str(input())
        result.append(find_sum(string_to_check))
    print(*result, sep='\n')
