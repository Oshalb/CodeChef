# count 1's in a string

# 011000100
if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        length_of_string = n = int(input())
        string_to_check = s = str(input())
        c = 0
        for i in range(n):
            destroyed = False
            if s[i] == '1':
                destroyed = True
            if i > 0 and s[i - 1] == '1':
                destroyed = True
            if i < n-1 and s[i + 1] == '1':
                destroyed = True
            if not destroyed:
                c += 1
        result.append(c)
    print(*result, sep='\n')
