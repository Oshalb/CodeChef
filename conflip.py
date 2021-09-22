# Single player coin flip game

# H H H H H
# T H H H H
# H T H H H
# T H T H H
# H T H T H
# T H T H T

"""
H H H H H H H H H H
T H H H H H H H H H
H T H H H H H H H H
T H T H H H H H H H
H T H T H H H H H H
T H T H T H H H H H
H T H T H T H H H H
T H T H T H T H H H
H T H T H T H T H H
T H T H T H T H T H
H T H T H T H T H T

H H H H H H
T H H H H H
H T H H H H
T H T H H H
H T H T H H
T H T H T H
H T H T H T
"""

for _ in range(int(input())):
    for a in range(int(input())):
        initail_state, number_of_rounds, which_side = map(int, input().rstrip().split())
        i, q, n = initail_state, number_of_rounds, which_side
        if q % 2 == 0 or i == n:
            print(q // 2)
        else:
            print(q // 2 + 1)
