# Meta variables
day = 3
year = 2024

# Packages
import re

# Read the data
file_path = f'../Data/{year}_Day{day}.txt'
f = open(file_path,'r')
data = f.read()

# Part 1: Parse mul cmds
# mul_cmds = re.findall('mul\(\d+,\d+\)',data)
# mul_results = [int(re.findall('\d+',i)[0]) * int(re.findall('\d+',i)[1]) for i in mul_cmds]
# mul_total = sum(mul_results)

# print(f'Part 1 Answer: The total is {mul_total}')

# Part 2: Parse do & don't cmds
all_cmds = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)",data)

is_active = 1
p1_result = 0
p2_result = 0

for i in range(len(all_cmds)):
    cmd = all_cmds[i]

    if cmd == "do()":
        is_active = 1
    elif cmd == "don't()":
        is_active = 0
    else:
        p1_result += int(re.findall('\d+',cmd)[0]) * int(re.findall('\d+',cmd)[1])
        p2_result += int(re.findall('\d+',cmd)[0]) * int(re.findall('\d+',cmd)[1]) * is_active


print(f'Part 1 Answer: The total is {p1_result}')
print(f'Part 2 Answer: The total is {p2_result}')

    