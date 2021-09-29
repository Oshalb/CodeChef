# Make every number in a list same using increment of one.

"""
1 2-
2 2
1 op

1 2 3-
2 3 3-
3 4- 3
4 4 4
3 op

1 2 3 4-
2 3 4 4-
3 4 5- 4
4 5 5 5-
5 6 6- 5
6 7- 6 6
7 7 7 7
6 op

1 2 3 4 5-
2 3 4 5 5-
3 4 5 6- 5
4 5 6 6 6-
5 6 7 7- 6
6 7 8- 7 7
7 8 8 8 8-
8 9 9 9- 8
9 10 10- 9 9
10 11- 10 10 10
11 11 11 11 11
10 op

1 2 3 4 5 6-
2 3 4 5 6 6-
3 4 5 6 7- 6
4 5 6 7 7 7-
5 6 7 8 8- 7
6 7 8 9- 8 8
7 8 9 9 9 9-
8 9 10 10 10- 9
9 10 11 11- 10 10
10 11 12- 11 11 11
11 12 12 12 12 12-
12 13 13 13 13- 12
13 14 14 14- 13 13
14 15 15- 14 14 14
15 16- 15 15 15 15
16 16 16 16 16 16
15 op

4 5 6-
5 6 6-
6 7- 6
7 7 7
"""


def get_operations(n, ls):
    s = sum(ls)
    m = min(ls)
    t = s - (n * m)
    return t


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        number_of_workers = int(input())
        list_of_salaries = list(map(int, input().rstrip().split()))
        result.append(get_operations(number_of_workers, list_of_salaries))
    print(*result, sep='\n')
