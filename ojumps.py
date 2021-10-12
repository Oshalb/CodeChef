# Additive increase 1 + 2 + 3

# 0
# 1 3 6
# 7 9 12
# 13 15 18
# 19 21 24
if __name__ == "__main__":
    number_of_steps = a = int(input())
    t = a % 6
    if a % 3 == 0:
        print("yes")
    elif t == 0 or t == 1:
        print("yes")
    else:
        print("no")
