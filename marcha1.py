# Sum of subset of a list.
from itertools import combinations


def count_notes(n, m, ln):
    if sum(ln) < m:
        return "No"
    else:
        ls = [num for i in range(1, n+1) for num in combinations(ln, i)]
        for i in ls:
            if sum(i) == m:
                return "Yes"
        return "No"


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        banknotes, amount_asked = map(int, input().rstrip().split())
        values_of_notes = []
        for a in range(banknotes):
            values_of_notes.append(int(input()))
        result.append(count_notes(banknotes, amount_asked, values_of_notes))
    print(*result, sep='\n')
