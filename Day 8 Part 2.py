import json
import functools

def pretty(matrix):
  print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
  
f = open("input 8.txt", "r")
input = f.read().split('\n')

patch = list(map(lambda row: list(map(lambda tree: int(tree), list(row))), input))
score = [[1] * len(patch[0]) for i in range(len(patch))]

score[0] = [0] * len(patch[0])
score[-1] = [0] * len(patch[0])
for i in range(1, len(patch) - 1):
  score[i][0] = 0
  score[i][-1] = 0

#pretty(patch)

for i in range(1, len(patch) - 1):
  for j in range(1, len(patch[0]) - 1):
    view = 0
    for i0 in reversed(range(i)):
      view += 1
      if patch[i0][j] >= patch[i][j]: break
    score[i][j] *= view
    
    view = 0
    for i0 in range(i + 1, len(patch)):
      view += 1
      if patch[i0][j] >= patch[i][j]: break
    score[i][j] *= view
    
    view = 0
    for j0 in range(j + 1, len(patch)):
      view += 1
      if patch[i][j0] >= patch[i][j]: break
    score[i][j] *= view
    
    view = 0
    for j0 in reversed(range(j)):
      view += 1
      if patch[i][j0] >= patch[i][j]: break
    score[i][j] *= view
      
  #print(maxEl)
#pretty(score)
#pretty(patch)

print(functools.reduce(lambda x, y: max(x, functools.reduce(max, y, 0)), score, 0))
