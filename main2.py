import consts, csv
import random
from Job import Job
from Person2 import Person






with open(consts.JOBPATH) as f:
    rawdata = list(csv.reader(f, delimiter=","))

data = rawdata[1:]
jobs = []

for i in range(len(data)):
    for j in range(1,11):
        data[i][j] = int(data[i][j])*consts.JOB_FACTOR_WEIGHTS[j-2]
    data[i][11] = set(map(lambda x: x.strip(), data[i][11].split(',')))
    coords = ("None", "None") if data[i][12] == "" else (float(data[i][12]), float(data[i][13]))
    jobs.append(Job(*data[i][:12], coords))



with open(consts.PERSONPATH) as f:
    rawpersons = list(csv.reader(f))

personlist = rawpersons[1:]
persons = []

for i in range(len(personlist)):
    for j in range(1,22):
        personlist[i][j] = float(personlist[i][j])*consts.PERSON_FACTOR_WEIGHTS[j-1]
    personlist[i][-1] = set(map(lambda x: x.strip(), personlist[i][-1].split(',')))
    persons.append(Person(*personlist[i]))




person1 = persons[20]

def calc_scores(person, jobsample=jobs):
    scores = person.scores(jobsample)
    # for score in scores:

    #     print(f"{person}; {score}")

    results = sorted(zip(scores, jobsample), key=lambda x: x[0])
    # bytags = {}

    # for i, result in enumerate(results):
    #     k = len(person1.tags.intersection(result[1].tags))
    #     if k not in bytags:
    #         bytags[k] = []
    #     bytags[k].append(result)
    


    return results

SEP = ";"

f = open(consts.OUTPUTPATH, "w")

jsample = jobs
f.write("id" + SEP + SEP.join("S" + str(j) + SEP + str(j) for j in range(len(jsample))) + "\n")
f.close()
def all_scores(jobsample=jobs):
    people_scores = []
    for i, person in enumerate(persons, start=1):
        f = open(consts.OUTPUTPATH, "a")
        score = calc_scores(person, jobsample)
        line = [SEP.join((str(pair[1].id) , str(pair[0]))) for pair in score]
        f.write(str(i) + SEP + SEP.join(line) + "\n")

        people_scores.append(score)
        print(f"{person} finished")
        f.close()
    return people_scores


# jsample = jobs[:2]


# print(calc_scores(person1, jsample))

final_scores = all_scores(jsample)
        

print("Finished!")
    


# print(person1)
# print()
# print(*map(lambda x: (x[0], str(x[1])), results), sep="\n")
# print()

# for key, value in bytags.items():
#     print(key)
#     print(*map(lambda x: (x[0], str(x[1])), value), sep="\n")
#     print()
