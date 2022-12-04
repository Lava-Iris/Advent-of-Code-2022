f = open("input 4.txt", "r")
input = f.read().split('\n')

sum = 0

for pair in input:
  pair = pair.split(',')
  section1 = pair[0].split('-')
  section2 = pair[1].split('-')
  
  min = section2 if int(section2[0]) < int(section1[0]) else section1
  max = section2 if min == section1 else section1
  
  sum += int(min[0] == max[0] or int(min[1]) >= int(max[0]))
      
print(sum)
