# one sequence in another


def check_subseq(m, w):
    lm, lw = len(m), len(w)
    if lm > lw:
        s, t = w, m
    else:
        s, t = m, w
    j = 0
    i = 0
    while i < len(s):
        while j < len(t):
            if t[j] == s[i]:
                break
            j += 1
        if j > len(t):
            return "NO"
        i += 1
        j += 1
    return "YES"


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        name_of_man, name_of_woman = map(str, input().rstrip().split())
        result.append(check_subseq(name_of_man, name_of_woman))
    print(*result, sep='\n')
