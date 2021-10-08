# pair of lengths

if __name__ == "__main__":
    number_of_chopsticks, min_length = map(int, input().rstrip().split())
    n, d = number_of_chopsticks, min_length
    lengths_to_check = ltc = []
    for _ in range(n):
        lengths_to_check.append(int(input()))
    ltc = sorted(ltc)
    c = 0
    i = 0
    while i < n-1:
        if ltc[i] >= ltc[i+1] - d:
            c += 1
            i += 2
        else:
            i += 1
    print(c)
