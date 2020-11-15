import csv
with open("data/jobdata.csv") as f:
    data = list(csv.reader(f))[1:]

tags = set()

for line in data:
    tags.update(map(lambda x: x.strip(), line[11].split(',')))

print(sorted(list(tags)))
