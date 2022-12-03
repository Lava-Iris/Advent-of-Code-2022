f = open("input 3.txt", "r")
input = f.read().split("\n")

sum = 0

for rucksack in input:
  for type in rucksack[: len(rucksack) // 2]:
    if type in rucksack[len(rucksack) // 2 :]: 
      if type.isupper():
        sum += ord(type) - 65 + 27
      else:
        sum += ord(type) - 97 + 1
      break
   
print(sum)
