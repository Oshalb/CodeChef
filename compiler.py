# correct semantic prifix  length

def check_prefix(s):
    t, ans = 0, 0
    for i, j in enumerate(s):
        if j == '<':
            t += 1
        else:
            t -= 1
        if t == 0:
            ans = max(ans, i+1)
        elif t < 0:
            break
    return ans


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        string_to_check = str(input())
        result.append(check_prefix(string_to_check))
    print(*result, sep='\n')
