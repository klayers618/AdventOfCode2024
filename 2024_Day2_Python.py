# Meta variables
day = 1
year = 2024

# Read the data
file_path = f'Data/{year}_Day{day}.txt'
f = open(file_path,'r')
data = f.read().splitlines()