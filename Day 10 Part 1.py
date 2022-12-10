f = open("input 10.txt", "r")
input = f.read().split('\n')

cycle = 1
X = 1
ans = 0

def add_cycle():
  global cycle, ans, X
  cycle += 1
  if cycle in [20, 60, 100, 140, 180, 220]:
    ans += cycle * X
  
for instruction in input:
  if instruction == 'noop':
    add_cycle()
  else:
    add_cycle()
    X += int(instruction.split(' ')[1])
    add_cycle()

print(ans)
