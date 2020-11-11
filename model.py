with open("data/data_notags.csv") as f:
    rawdata = f.readlines()[1:]

data = []
for line in rawdata:
    data.append(line.split(','))

for j in range(len(data)):
    for i in range(1, len(data[j])):
        data[j][i] = data[j][i].strip()
        if data[j][i].isdigit(): data[j][i] = int(data[j][i])
        elif data[j][i] in ["false", "true"]: data[j][i] = data[j][i] == "true"
        if data[j][i] == "NA": data[j][i] = None

#for line in data:
#    print(*(line[1:]), sep='\t')
tags = ["computers", "programming", "music"]

#            Physical   Remote  Sociality   Computer    Urbanity    $/h Tags
person  =   [1,         1,      2,          4,          2,          20]
weights =   [0.7,       0.0,    0.3,        0.7,        0.8,        0.7]

distance = [0 for _ in range(len(data))]

for i in range(len(data)):
    for j in range(1,len(data[i])):
        if data[i][j] != None: distance[i] += weights[j-1]*abs(person[j-1]-data[i][j])**2

results = sorted(zip(distance, [x[0] for x in data]))
print(*results, sep='\n')
