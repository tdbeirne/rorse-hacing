import csv


win_rates = {}

# populate win_rate_dict
with open("data/runs_augmented.csv", "r") as r:
    runs = csv.reader(r, delimiter=",")
    next(runs)

    for run in runs:
        key = int(run[4]) # 2 is horse_id, 3 is trainer_id, 4 is jockey_id
        if key not in win_rates:
            win_rates[key] = [int(run[12])] # 12 is won
        else:
            win_rates[key].append(int(run[12])) # 12 is won

# load csv into memory and aguement cells
with open("data/runs_augmented.csv", "r") as r:
    runs = csv.reader(r, delimiter=",")

    lines = list(runs)

    for line in lines:
        if line is lines[0]: # header row
            continue
        performances = win_rates[int(line[3])]  # 2 is horse_id, 3 is trainer_id, 4 is jockey_id
        win_rate = round(sum(performances) / len(performances), 3)
        line[7] = win_rate # 5 is horse_win, 6 is trainer, 7 is jockey
        line[10] = len(performances) # 8 is horse_games, 9 is trainer, 10 is jockey
        
# dump memory back into new file
with open("data/runs_augmented.csv", "w", newline='') as w:
    writer = csv.writer(w, delimiter=",")
    writer.writerows(lines)