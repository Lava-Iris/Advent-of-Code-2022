f = open("input 3.txt", "r")
input = f.read().split("\n")

sum = 0
i = 0

while i < len(input):
  rucksack1 = input[i]
  rucksack2 = input[i + 1]
  rucksack3 = input[i + 2]
  for type in rucksack1:
    if type in rucksack2 and type in rucksack3: 
      if type.isupper():
        sum += ord(type) - 65 + 27
      else:
        sum += ord(type) - 97 + 1
      break
  i += 3
      
print(sum)

  
