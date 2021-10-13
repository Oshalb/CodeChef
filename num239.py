# Check last digit

# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27 28 29 30

t = int(input())
for _ in range(t):
    a, b = map(int, input().rstrip().split())
    c = 0
    for i in range(a, b+1):
        t = i % 10
        if t == 2 or t == 3 or t == 9:
            c += 1
    print(c)
