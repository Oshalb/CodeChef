# equal number of candies
# Always check edge cases

if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        number_of_candies, number_of_students = map(int,  input().rstrip().split())
        n, k = number_of_candies, number_of_students
        if k == 0:
            print(0, n)
        else:
            a, b = divmod(n, k)
            print(a, b)
