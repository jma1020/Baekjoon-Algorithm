n = int(input())

fibonacci = [0, 1]
for i in range(2, n+1):
    num = fibonacci[i-2] + fibonacci[i-1]
    fibonacci.append(num)
    print(i)
    print(fibonacci)