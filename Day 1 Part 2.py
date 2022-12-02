import math

f = open("input.txt", "r")
input = f.read().split("\n\n")

max = [-math.inf, -math.inf, -math.inf]

for line in input:
  line = line.split()
  sum = 0
  for inp in line:
    sum +=int(inp)

  if sum > max[0]:
    if sum > max[1]:
      if sum > max[2]:
        max[0] = max[1]
        max[1] = max[2]
        max[2] = sum
      else:
        max[0] = max[1]
        max[1] = sum
    else:
      max[0] = sum
      
ans = 0
for int in max:
  ans += int

print(ans)

  
