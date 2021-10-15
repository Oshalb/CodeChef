# Prime numbers
# a(n) = 4 * n + 1

def find_winner(n):
    return "ALICE" if n % 4 == 1 else "BOB"


if __name__ == "__main__":
    number_of_testcases = int(input())
    result = []
    for _ in range(number_of_testcases):
        number_of_moves = int(input())
        result.append(find_winner(number_of_moves))
    print(*result, sep='\n')
