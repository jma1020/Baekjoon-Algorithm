index = list(int(input()) for _ in range(9))

sum = sum(index)


def combi(index):
  for i in range(len(index)):
    for j in range(i+1,len(index)):
      if sum - (index[i]+ index[j]) == 100:
        remove = {index[i],index[j]}
        result = [s for s in index if s not in remove]
        result.sort()

        for item in result:
          print(item)
        return

combi(index)

# 기존 코드는 함수가 없이 break 하나로 탈출했다, 근데 print하고도 이중반복문을 계속 돌아서 그런지 그게 문제가 되어서 틀렸다고 그냥 함수를 해서 return을 넣어줬다 