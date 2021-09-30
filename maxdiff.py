# Max diff of two parts of a list

def find_diff(w, k):
    w = sorted(w)
    f = w[:k]
    s = w[k:]
    ff = w[-1:-(k+1):-1]
    ss = w[:-k]
    sum_f, sum_s, sum_ff, sum_ss = \
        sum(f), sum(s), sum(ff), sum(ss)
    return max(abs(sum_f - sum_s), abs(sum_ff - sum_ss))


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        number_of_weights, seperating_value = map(int, input().rstrip().split())
        list_of_weights = list(map(int, input().rstrip().split()))
        result.append(find_diff(list_of_weights, seperating_value))
    print(*result, sep='\n')
