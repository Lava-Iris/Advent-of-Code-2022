f = open("input 2.txt", "r")
input = f.read().split('\n')

sum = 0
score = {'X': 1, 'Y': 2, 'Z': 3}
win = {'A' : 'Y', 'B': 'Z', 'C': 'X'}
draw = {'A' : 'X', 'B': 'Y', 'C': 'Z'}

for line in input:
  opp = line[0]
  me = line[2]
  sum += score[me]
  
  if me == win[opp]:
    sum += 6
  elif me == draw[opp]:
    sum += 3

print(sum)
