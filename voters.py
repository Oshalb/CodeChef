# compare three different list's to find same items

if __name__ == "__main__":
    n1, n2, n3 = map(int, input().rstrip().split())
    dict_to_check = d = {}
    for _ in range(n1+n2+n3):
        i = int(input())
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    c = 0
    for i in d:
        if d[i] >= 2:
            c += 1
    print(c)
    for i in sorted(d):
        if d[i] >= 2:
            print(i)
