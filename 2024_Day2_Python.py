# Meta variables
day = 2
year = 2024

# Packages
import numpy as np

# Read the data
file_path = f'../Data/{year}_Day{day}.txt'
f = open(file_path,'r')
data = f.read().splitlines()

data_list = [x.split() for x in data]
data_list = [[int(x) for x in data_list[i]] for i in range(len(data_list))]

# Find difference between values & test for safety
diff_list = [np.diff(data_list[i]) for i in range(len(data_list))]

# Loop and count the number of safe reports.
# This was my original approach, but I'd like to determine WHICH reports are safe instead to help limit the loops for Part 2
    # safety_cnt = 0

    # for i in range(len(diff_list)):
    #     increases = [x for x in diff_list[i] if x >= 0]
    #     decreases = [y for y in diff_list[i] if y <= 0]

    #     if len(increases) == len(diff_list[i]) and max(diff_list[i]) <= 3 and min(diff_list[i]) >= 1:
    #         safety_cnt += 1
    #     elif len(decreases) == len(diff_list[i]) and max(diff_list[i]) <= -1 and min(diff_list[i]) >= -3:
    #         safety_cnt += 1

    # print(f'Part 1 Answer: There are {safety_cnt} safe reports.')

safety_determinations = []

for i in range(len(diff_list)):
    increases = [x for x in diff_list[i] if x > 0]
    decreases = [y for y in diff_list[i] if y < 0]

    if len(increases) == len(diff_list[i]) and max(diff_list[i]) <= 3 and min(diff_list[i]) >= 1:
        safety_determinations.append(1)
    elif len(decreases) == len(diff_list[i]) and max(diff_list[i]) <= -1 and min(diff_list[i]) >= -3:
        safety_determinations.append(1)
    else:
        safety_determinations.append(0)

safe_reports = [data_list[i] for i in range(len(data_list)) if safety_determinations[i] == 1]
unsafe_reports = [data_list[i] for i in range(len(data_list)) if safety_determinations[i] == 0]

p1_safe_report_cnt = len(safe_reports)

print(f'Part 1 Answer: There are {p1_safe_report_cnt} safe reports.')

# Test safety again for unsafe reports by eliminating values from the report

mod_safe_report_cnt = 0

for i in range(len(unsafe_reports)):
    report = unsafe_reports[i]

    # Modify each report & test safety (turn this into a function for use in p1 and p2)
    for j in range(len(report)):
        mod_report = [report[k] for k in range(len(report)) if k != j]
        diff_list = [x for x in np.diff(mod_report)]

        increases = [x for x in diff_list if x > 0]
        decreases = [y for y in diff_list if y < 0]

        if len(increases) == len(diff_list) and max(diff_list) <= 3 and min(diff_list) >= 1:
            mod_safe_report_cnt += 1
            break # Rework this to use a condition to add to the counter instead of breaking the loop
        elif len(decreases) == len(diff_list) and max(diff_list) <= -1 and min(diff_list) >= -3:
            mod_safe_report_cnt += 1
            break

p2_safe_report_cnt = p1_safe_report_cnt + mod_safe_report_cnt

print(f'Part 2 Answer: There are {p2_safe_report_cnt} safe reports')