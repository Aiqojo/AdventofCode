# Read input
with open("t1.txt", "r") as f:
    data = f.readlines()

# Parse input
calories = []
cur_elf = []
for line in data:
    line = line.strip()
    if line == "":
        calories.append(sum(cur_elf))
        cur_elf = []
    else:
        cur_elf.append(int(line))
calories.append(sum(cur_elf))

# Find the elf with the most calories
max_calories = max(calories)
print(max_calories)
