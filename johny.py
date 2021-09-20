# Position of a number in list after sorting

def binary_search(lo, hi, k):
    mid = (lo + hi) // 2
    if k == ls[mid]:
        return mid + 1
    elif k > ls[mid]:
        return binary_search(mid + 1, hi, k)
    elif k < ls[mid]:
        return binary_search(lo, mid - 1, k)


for _ in range(int(input())):
    number_of_songs = n = int(input())
    length_of_songs = ln = list(map(int, input().rstrip().split()))
    position_of_uncle = pu = int(input()) - 1
    value_of_uncle = vn = ln[pu]
    ls = sorted(ln)
    result = binary_search(0, n, vn)
    print(result)
