import consts, csv
from Job import Job
from Person import Person

with open(consts.DATAPATH) as f:
    rawdata = list(csv.reader(f))

data = rawdata[1:]
jobs = []

for i in range(len(data)):
    for j in range(1,11):
        data[i][j] = int(data[i][j])
    data[i][11] = list(map(lambda x: x.strip(), data[i][11].split(',')))
    jobs += Job.nJob(data[i][1], [data[i][0]] + data[i][2:])

print(*jobs, sep="\n")
