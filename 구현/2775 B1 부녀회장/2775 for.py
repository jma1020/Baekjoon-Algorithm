T = int(input())

for _ in range(T):

    k = int(input())

    n = int(input())

    people = [ i for i in range(1, n+1)]
    print(people)
    for __ in range(k):

        for j in range(1,n):

            people[j] += people[j-1]
            print(people)
            print(people[j])
            print(people[j-1])

    print(people[-1])

    # 1층 3호에 값 + 2층 2호의 값 을 더하면 == 2층 3호을 구할 수 있다