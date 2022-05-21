def get_num_of_hansoo(n):
    count = 0  # 한수 갯수 세는 변수
    for i in range(1, n+1):
        if 1 <= i <= 99:  # 한 자리 수나 두 자리수 일 때
            count += 1
        elif i == 1000:  # 4자리 수 일 때
            pass
        else:  # 세 자리 수 일 때
            l = list(map(int, str(i)))
            if l[1] == (l[0] + l[2]) / 2:  # 등차수열일 경우 성립하는 공식
                count += 1
    return count


N = int(input())
print(get_num_of_hansoo(N))