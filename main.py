import consts, csv
from Job import Job
from Person import Person

with open(consts.DATAPATH) as f:
    rawdata = list(csv.reader(f))

data = rawdata[1:]
jobs = []

for i in range(len(data)):
    for j in range(1,10):
        data[i][j] = int(data[i][j])
    data[i][10] = list(map(lambda x: x.strip(), data[i][10].split(',')))
    jobs += Job.nJob(3, data[i][:-1])

print(*jobs, sep="\n")
