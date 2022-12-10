f = open("input 10.txt", "r")
input = f.read().split('\n')

def pretty(matrix):
  print('\n'.join([''.join([str(cell) for cell in row]) for row in matrix]))

cycle = 1
X = 1

curr_pixel = 0
CRT = [['.'] * 40 for _ in range(6)]

def add_cycle():
  global cycle, curr_pixel, X
  cycle += 1
  curr_pixel += 1
  
  hor = curr_pixel % 40
  vert = curr_pixel // 40
  
  if hor in [X - 1, X, X + 1]:
    CRT[vert][hor] = '#'
  
for instruction in input:
  if instruction == 'noop':
    add_cycle()
  else:
    add_cycle()
    X += int(instruction.split(' ')[1])
    add_cycle()

pretty(CRT)
