f = open("input 9.txt", "r")
input = f.read().split('\n')

knots = [[0, 0] for i in range(10)]
visited = {(0, 0)}
#print(knots)

def is_touching(head, tail):
  return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1

sign = lambda x: 1 if x > 0 else -1
head = knots[0]
tail = knots[-1]

def move_tail(head, tail):
  if is_touching(head, tail): return tail
  elif abs(head[0] - tail[0]) == 0:
    tail[1] = (head[1] + tail[1]) // 2
  elif abs(head[1] - tail[1]) == 0:
    tail[0] = (head[0] + tail[0]) // 2
  else:
    tail[0] = tail[0] + sign(head[0] - tail[0])
    tail[1] = tail[1] + sign(head[1] - tail[1])
  return tail


for move in input:
  #print(move)
  move = move.split(" ")
  dir = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}

  for _ in range(int(move[1])):
    head[0] = head[0] + dir[move[0]][0]
    head[1] = head[1] + dir[move[0]][1]
    
    for i in range(1, 10):
      #print(knots)
      knots[i] = move_tail(knots[i - 1], knots[i])

    visited.add(tuple(tail))
  #print(knots)
  
print(len(visited)
