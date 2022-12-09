import json
import functools

def pretty(matrix):
  print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
  
f = open("input 8.txt", "r")
input = f.read().split('\n')

patch = list(map(lambda row: list(map(lambda tree: int(tree), list(row))), input))
visible = [[False] * len(patch[0]) for i in range(len(patch))]

visible[0] = [True] * len(patch[0])
visible[-1] = [True] * len(patch[0])

for i in range(1, len(patch) - 1):
  visible[i][0] = True
  visible[i][-1] = True

maxRow = patch[0][1:-1].copy()
for i in range(1, len(patch) - 1):
  maxEl = patch[i][0]
  for j in range(1, len(patch[0]) - 1):
    if patch[i][j] > maxEl:
      maxEl = patch[i][j]
      visible[i][j] = True
      
    if patch[i][j] > maxRow[j - 1]:
      maxRow[j - 1] = patch[i][j]
      visible[i][j] = True

maxRow = patch[-1][1:-1].copy()
for i in reversed(range(1, len(patch) - 1)):
  maxEl = patch[i][-1]
  for j in reversed(range(1, len(patch[0]) - 1)):
    if patch[i][j] > maxEl:
      maxEl = patch[i][j]
      visible[i][j] = True
      
    if patch[i][j] > maxRow[j - 1]:
      maxRow[j - 1] = patch[i][j]
      visible[i][j] = True
  #print(maxEl)
#pretty(visible)
#pretty(patch)

print(functools.reduce(lambda x, y: x + functools.reduce(lambda a, b: a + int(b), y, 0), visible, 0))
