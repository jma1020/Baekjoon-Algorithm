a, b, height = map(int,input().split())

import math
day = math.ceil((height-b) / (a-b))
print(day)