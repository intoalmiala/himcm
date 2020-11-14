import consts, csv
from Job import Job
from Person import Person




with open(consts.JOBPATH) as f:
    rawdata = list(csv.reader(f))

data = rawdata[1:]
jobs = []

for i in range(len(data)):
    for j in range(1,11):
        data[i][j] = int(data[i][j])
    data[i][11] = list(map(lambda x: x.strip(), data[i][11].split(',')))
    jobs += Job.nJob(data[i][1], [data[i][0]] + data[i][2:])




with open(consts.PERSONPATH) as f:
    rawpersons = list(csv.reader(f))

personlist = rawpersons[1:]
persons = []

for i in range(len(personlist)):
    for j in range(1,-1):
        personlist[i][j] = float(personlist[i][j])
    personlist[i][-1] = list(map(lambda x: x.strip(), personlist[i][-1].split(',')))
    persons.append(Person(*personlist[i]))




person1 = persons[0]
scores = []

for job in jobs:
    scores.append(person1.score(job))

results = sorted(zip(scores, jobs))

print(*results, sep="\n")
