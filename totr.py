# english language permutation

def find_trans(s, d):
    t = ""
    for i in s:
        if i in d:
            t += d[i]
        else:
            t += i
    return t


if __name__ == "__main__":
    inp = list(map(str, input().rstrip().split()))
    number_of_testcases = int(inp[0])
    p = inp[1]
    result = []
    dit = {'_': ' '}
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for h, k in enumerate(lowercase):
        dit[k] = p[h]
    pu = p.upper()
    for h, k in enumerate(uppercase):
        dit[k] = pu[h]
    for _ in range(number_of_testcases):
        string_to_check = str(input())
        result.append(find_trans(string_to_check, dit))
    print(*result, sep='\n')
