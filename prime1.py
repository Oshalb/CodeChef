# List Prime numbers
from math import sqrt

for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    result = set()
    a = max(a, 2)
    for i in range(2, int(sqrt(b))+1):
        for j in range(max(a//i,2), (b//i)+1):
            result.add(i * j)
    for i in range(a, b+1):
        if i not in result:
            print(i)
    print()
