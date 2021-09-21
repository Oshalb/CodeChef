# Count number of jobs left

for _ in range(int(input())):
    total_number_of_jobs, jobs_completed = map(int, input().rstrip().split())
    n, m = total_number_of_jobs, jobs_completed
    checklist = c = {i: False for i in range(1, n+1)}
    done_list = list(map(int, input().rstrip().split()))
    for i in done_list:
        c[i] = True
    a, b = set(), set()
    job = 1
    for i in c:
        if not c[i]:
            if job == 1:
                a.add(i)
            else:
                b.add(i)
            job ^= 1
    a = sorted(a)
    b = sorted(b)
    print(*a)
    print(*b)
