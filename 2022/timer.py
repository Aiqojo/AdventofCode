import os
import time

# Set the directory to the root of your Advent of Code project
root_dir = os.getcwd()

times = []

for i in range(1, 25):
    try:
        # Set the current directory to the day's folder
        day_dir = os.path.join(root_dir, "d" + str(i))
        os.chdir(day_dir)

        # Get the path to the day's script
        script_path = os.path.join(day_dir, "d" + str(i) + ".py")

        # Time how long it takes to run the script
        start_time = time.time()
        os.system("python " + script_path)
        end_time = time.time()

        times.append(end_time - start_time)
    except:
        pass

# Print the running time
for i, time in enumerate(times):
    print(f"\n Day {i + 1} took {round(time, 6)} seconds to run.")

# Print the average running time
print(f"\n The average running time was {round(sum(times) / len(times), 6)} seconds.")

# Print the total running time
print(f"\n The total running time was {round(sum(times), 6)} seconds.")
