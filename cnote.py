# Claculate pages and price for books

for _ in range(int(input())):
    x, y, k, n = map(int, input().rstrip().split())
    pp = []
    for i in range(n):
        p, c = map(int, input().rstrip().split())
        pp.append((p, c))
    for i, j in pp:
        if i >= x - y and j <= k:
            print("LuckyChef")
            break
    else:
        print("UnluckyChef")
