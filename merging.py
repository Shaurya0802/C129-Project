import csv

file_1 = "bright_stars.csv"
file_2 = "unit_converted_stars.csv"

dataset_1 = []
dataset_2 = []

with open(file_1, "r", encoding="utf8") as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        dataset_1.append(i)

with open(file_2, "r", encoding="utf8") as f:
    csv_reader = csv.reader(f)

    for j in csv_reader:
        dataset_2.append(j)

header_1 = dataset_1[0]
header_2 = dataset_2[0]

data_1 = dataset_1[1:]
data_2 = dataset_2[1:]

header = header_1 + header_2

data = []

for k in data_1:
    data.append(k)

for l in data_2:
    data.append(l)

with open("complete.csv", "w", encoding="utf8") as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(header)
    csv_writer.writerows(data)