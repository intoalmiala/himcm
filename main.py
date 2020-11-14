import consts, csv
import random
from Job import Job
from Person import Person




with open(consts.JOBCOORDPATH) as f:
    coords = list(csv.reader(f))

for i, line in enumerate(coords):
    if line[0] == "None":
        coords[i] = None
    else:
        coords[i] = tuple(map(float, line))

with open(consts.JOBPATH) as f:
    rawdata = list(csv.reader(f))

data = rawdata[1:]
jobs = []
coord_index = 0

for i in range(len(data)):
    for j in range(1,11):
        data[i][j] = int(data[i][j])*consts.JOB_FACTOR_WEIGHTS[j-1]
    data[i][11] = list(map(lambda x: x.strip(), data[i][11].split(',')))
    jobs += Job.nJob(data[i][1], [data[i][0]] + data[i][2:], coords[coord_index:coord_index+data[i][1]])
    coord_index += data[i][1]




with open(consts.PERSONPATH) as f:
    rawpersons = list(csv.reader(f))

personlist = rawpersons[1:]
persons = []

for i in range(len(personlist)):
    for j in range(1,22):
        personlist[i][j] = float(personlist[i][j])*consts.PERSON_FACTOR_WEIGHTS[j-1]
    personlist[i][-1] = list(map(lambda x: x.strip(), personlist[i][-1].split(',')))
    persons.append(Person(*personlist[i]))




with open("personcoords.csv", "w") as f:
    for person in persons:
        f.write(';'.join(map(str, person.pos))+"\n")




person1 = persons[0]
scores = []
jobsample = jobs#random.sample(jobs, 8)

for job in jobsample:
    scores.append(person1.score(job))
    print(scores[-1])

results = sorted(zip(scores, map(str, jobsample)), key=lambda x: x[0])

print(person1)
print()
print(*results, sep="\n")
