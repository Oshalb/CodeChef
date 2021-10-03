# list of increasing number to a limit

def calculate_list(a, n, k):
    r = []
    n += 1
    for _ in range(k):
        r.append(a%n)
        a //= n
    return r


if __name__ == "__main__":
    bombarded_particles, max_particles, number_of_chambers = map(int, input().rstrip().split())
    result = calculate_list(bombarded_particles, max_particles, number_of_chambers)
    print(*result, sep=' ')
