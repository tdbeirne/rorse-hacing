import csv



# populate win_rate_dict
with open("data/runs_augmented.csv", "r") as r:
    runs = csv.reader(r, delimiter=",")
    next(runs)