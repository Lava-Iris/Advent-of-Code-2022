#import json
import math

f = open("input 7.txt", "r")
input = f.read().split('\n')

dir = '/'
is_command = lambda line: line[0] == '$'
is_cd = lambda line: line[1] == 'cd'
is_ls = False
structure = {'/':{'size': 0, 'path': [], 'children': {}}}
curr_dir = structure[dir]

def find_dir(path):
  curr = structure['/']
  for dir in path[1:]:
    curr = curr['children'][dir]
  return curr

def update_size(size):
  curr_dir['size'] += size
  curr = structure
  #print(curr_dir['path'])
  for dir2 in curr_dir['path']:
    #print(dir2)
    #print(curr)
    curr[dir2]['size'] += size
    curr = curr[dir2]['children']

for line in input:
  #print(line)
  line = line.split(' ')
  if is_command(line):
    if is_cd(line):
      #print(json.dumps(structure, indent = 4))
      #print(curr_dir)
      dir = line[2]
      if line[2] == '..': 
        dir = curr_dir['path'][-1]
        curr_dir = find_dir(curr_dir['path'])
      elif line[2] == '/': 
        dir = '/'
        curr_dir = structure['/']
      else:
        dir = line[2]
        curr_dir = curr_dir['children'][dir]
      
      is_ls = False
    else:
      is_ls = True
  else:
    if (not is_ls) : continue
    if line[0] == 'dir':
      curr_dir['children'][line[1]] = {'size': 0, 'path': curr_dir['path'] + [dir], 'children': {}}
    else:
      update_size(int(line[0]))
  
#print(json.dumps(structure, indent = 4))

space_needed = 30000000 - (70000000 - structure['/']['size'])
#print(space_needed)

min = math.inf

def DFS(curr):
  global min
  for dir in curr:
    size = curr[dir]['size']
    if size > space_needed and size < min:
      min = size
    DFS(curr[dir]['children'])

DFS(structure)
print(min)
