import csv


with open("data/runs_augmented.csv", "r") as r:
    runs = csv.reader(r, delimiter=",")
    next(runs)

    with open("data/races2.csv", "r") as r:
        races = csv.reader(r, delimiter=",")
        next(races)

        # Somehow stitch together the two datasets???


quit() # do you dont actually create the file below during testing

# dump memory back into new file
with open("data/runs_and_races.csv", "w", newline='') as w:
    writer = csv.writer(w, delimiter=",")
    writer.writerows(lines)