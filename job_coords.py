import pandas as pd

COORDS = "jobcoordsoutput.csv"
OTHERDATA = "data/jobdatanew.csv"

coords = pd.read_csv(COORDS, delimiter=";", na_values="None")

data = pd.read_csv(OTHERDATA, delimiter=",")

data = data.loc[data.index.repeat(data["Frequency"])].reset_index()
data = data.rename({"index": "Id", "Lat": "PosX", "Lon": "PosY"}, axis=1)


newdata = pd.concat((data, coords), axis=1)
newdata = newdata[["Job title", "Id", *list(newdata.columns.values)[2:]]]
# print(newdata)
newdata.to_csv("jobslistfinal.csv", index=False)