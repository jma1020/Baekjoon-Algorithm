examCount = int(input())

scoreList = list(map(int,input().split()))[:examCount]


maxScore = max(scoreList)
for i in range(len(scoreList)):
  scoreList[i] = scoreList[i]/maxScore*100

print(sum(scoreList)/examCount)