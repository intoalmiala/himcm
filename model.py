import consts
import csv
import numpy as np

# luetaan data
with open(consts.FILEPATH) as f:
    data = np.array(list(csv.reader(f, delimiter=',')), dtype=object)[1:]

# käsitellään data
entry_tags = list(map(lambda x: x.split(', '), data[:,-1]))
data = data[:,:-1]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j].isdigit():
            data[i][j] = int(data[i][j])
data[data == "true"] = 1
data[data == "false"] = 0
data[data == "NA"] = None

# otetaan käyttäjädata
#           Physical    Remote  Sociality   Computer    Urbanity    $/h     Hours   Flexibility Gig
person  =  [1,          0,      2,          0,          3,          20,     30,     3,          0]
weights =  [0.9,        0.1,    0.7,        1.0,        0.9,        1.0,    0.7,    0.6,        1]

# lasketaan pisteet
scores = np.zeros(len(data))
for i in range(len(data)):
    for j in range(len(data[i,1:])):
        if data[i, 1+j] is None: continue
        scores[i] += weights[j] * consts.ATTRIBUTE_WEIGHTS[j] * abs(person[j] - data[i, 1+j])**2

results = np.array(sorted(list(zip(scores, data[:,0]))))
print(*results, sep='\n')

