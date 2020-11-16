from Job import Job
import consts
import csv

with open(consts.JOBCOORDPATH) as f:
    coords = list(csv.reader(f))

for i, line in enumerate(coords):
    if line[0] == "None":
        coords[i] = None
    else:
        coords[i] = tuple(map(float, line))

with open(consts.JOBPATH) as f:
    rawdata = list(csv.reader(f, delimiter=","))

data = rawdata[1:]
jobs = []
coord_index = 0

for i in range(len(data)):
    for j in range(1,11):
        data[i][j] = int(data[i][j])
    data[i][-1] = set(map(lambda x: x.strip(), data[i][-1].split(',')))
    jobs += Job.nJob(data[i][1], [data[i][0]] + data[i][1:], coords[coord_index:coord_index+data[i][1]])
    coord_index += data[i][1]


with open("jobslist.csv", "a") as out:
    i = 1
    for job in jobs:
        pos = (None, None) if job.pos is None else job.pos
        l =  [job.title, i, job.pay, job.hours, job.phys, job.soc, job.flex, job.conc, job.mono, job.gig, job.remote, job.tags, pos[0], pos[1]]

        out.write(";".join(str(k) for k in l) +  "\n")
        i += 1