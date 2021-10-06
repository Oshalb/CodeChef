# sum of n numbers

if __name__ == "__main__":
    number_of_menbers = n = int(input())
    list_of_colections = lc = list(map(int, input().rstrip().split()))
    slc = sum(lc)
    t = (n * (n + 1)) // 2
    print("YES" if slc == t else "NO")
