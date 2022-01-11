# ATM amount withdrawl
x, a = map(float, input().split())
if x+.50 > a or x % 5 != 0:
    print(a)
else:
    print(a-0.50 - x)
