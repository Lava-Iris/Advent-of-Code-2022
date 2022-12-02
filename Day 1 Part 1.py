import math

f = open("input.txt", "r")
input = f.read().split("\n\n")

max = -math.inf

for line in input:
  sum = 0
  for inp in line.split(): sum +=int(inp)
  if sum > max: max = sum
    
print(max)
