f = open("input 6.txt", "r")
input = f.read()

n = 14

prev_3 = [0] * (n - 1)
pointer = 0

for i in range(n - 1):
  prev_3[i] = input[i]
  
for i in range(n - 1, len(input)):
  if input[i] not in prev_3 and len(prev_3) == len(set(prev_3)):
    print(i + 1)
    break
  else:
    prev_3[pointer] = input[i]
    pointer = 0 if pointer == n - 2 else pointer + 1
