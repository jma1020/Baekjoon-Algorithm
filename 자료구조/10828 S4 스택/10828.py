import sys
N = int(sys.stdin.readline())

stack = []

def push(a):
  stack.append(a)

def pop():
  if len(stack) == 0:
    print(-1)
  else:
    print(stack.pop())

def top():
  if len(stack) == 0:
    print(-1)
  else:
    print(stack[-1])

def size():
  print(len(stack))

def empty():
  if len(stack) == 0:
    print(1)
  else:
    print(0)

for _ in range(N):
  inp = sys.stdin.readline().split()
  print(inp)
  if inp[0] == "push":
    push(int(inp[1]))
  elif inp[0] == "pop":
    pop()
  elif inp[0] == "top":
    top()
  elif inp[0] == "size":
    size()
  else:
    empty()
