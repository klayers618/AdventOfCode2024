# Meta variables
day = 1
year = 2024

# Libraries
from collections import Counter

# Read the data
file_path = f'Data/{year}_Day{day}.txt'
f = open(file_path,'r')
data = f.read().splitlines()

# Create two separate lists
list1 = [int(x.split()[0]) for x in data]
list2 = [int(x.split()[1]) for x in data]

# Sort the lists based on value
list1.sort()
list2.sort()

# Compute number of appearances in 2nd list by value
value_counts = Counter(list2)

# Compute distance & similarity between values in the lists
total_distance = 0
total_similarity = 0

for i in range(len(list1)):
    val1 = list1[i]
    val2 = list2[i]
    distance = abs(val2-val1)

    num_appearances = value_counts[val1]
    similarity_score = val1 * num_appearances
    
    total_distance += distance
    total_similarity += similarity_score

# Return puzzle answers
print(f'Part 1 Answer: The total distance between the files is {total_distance}')
print(f'Part 2 Answer: The similarity score between the files is {total_similarity}')
