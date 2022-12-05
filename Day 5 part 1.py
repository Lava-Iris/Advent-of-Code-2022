def pretty(matrix):
  print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

f = open("input 5.txt", "r")
input = f.read().split('\n\n')
init = input[0].split('\n') #initial state of stacks
dirs = list(map(lambda x: x.split(' '), input[1].split('\n'))) #directions to move the crates

numStacks = len(init[-1])//4 + 1
initArr = [[0]*numStacks for i in range(len(init) - 1)] #state of stacks in 2-d array (list) form
top = [0]*numStacks #top crate of each stack

#initialising initArr
for i in reversed(range(len(init) - 1)):
  row = init[len(init) - i - 2]
  j = 1
  
  while j < len(row):
    initArr[i][j//4] = row[j]
    if top[j//4] == 0 and row[j] != ' ':
      top[j//4] = (row[j], i)
    j += 4

#print(top)
#pretty(initArr)

#moving crates according to directions
for dir in dirs:
  #print(dir)
  num = int(dir[1]) #number of crates to move
  stack_from = int(dir[3]) - 1
  stack_to = int(dir[5]) - 1
    
  #indices of crates that will move
  from_is = list(reversed(range(top[stack_from][1] - num + 1, top[stack_from][1] + 1)))
  to_is = range(top[stack_to][1] + 1, top[stack_to][1] + num + 1)
  #print(list(from_is), list(to_is))
  
  #moving the stacks
  for i in range(num):
    if (to_is[i] > len(initArr) - 1):
      initArr.append([' ']*numStacks)
      
    initArr[to_is[i]][stack_to] = initArr[from_is[i]][stack_from]
    initArr[from_is[i]][stack_from] = ' '
    
  #updating the top crate of the changed stacks
  top[stack_from] = (initArr[from_is[-1] - 1][stack_from], from_is[-1] - 1)
  top[stack_to] = (initArr[to_is[-1]][stack_to], to_is[-1])
  #pretty(initArr)
  #pretty(top)

print("".join([row[0] for row in top]))
