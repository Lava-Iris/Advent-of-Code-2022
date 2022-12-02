f = open("input 2.txt", "r")
input = f.read().split('\n')

sum = 0
score = {'X': 0, 'Y': 3, 'Z': 6}
next = {'X': 2, 'Y': 0, 'Z': 1}
score2 = {'A' : 1, 'B': 2, 'C': 3}
eq = lambda x : 3 if x == 0 else x

for line in input:
  opp = line[0]
  win = line[2]
  #print(score2[opp], win, score[win], eq((score2[opp] + next[win]) % 3))
  sum += score[win]
  sum += eq((score2[opp] + next[win]) % 3)
      
print(sum)
