import numpy as np
import pandas as pd
import itertools as it
import math

pclass = [1,2,3]
sex = ["male", "female"]
ages = [
{"lower" : 0, "higher" : 1},
{"lower" : 2, "higher" : 3},
{"lower" : 4, "higher" : 5},
{"lower" : 6, "higher" : 8},
{"lower" : 9, "higher" : 11},
{"lower" : 12, "higher" : 14},
{"lower" : 15, "higher" : 18},
{"lower" : 19, "higher" : 21},
{"lower" : 22, "higher" : 26},
{"lower" : 27, "higher" : 31},
{"lower" : 32, "higher" : 36},
{"lower" : 37, "higher" : 41},
{"lower" : 42, "higher" : 46},
{"lower" : 47, "higher" : 51},
{"lower" : 52, "higher" : 56},
{"lower" : 57, "higher" : 61},
{"lower" : 62, "higher" : 66},
{"lower" : 67, "higher" : 71},
{"lower" : 72, "higher" : 76},
{"lower" : 77, "higher" : 100},
]
sibsps = [0,1,2,3,4,5,6,7,8]
parchs = [0,1,2,3,4,5,6]
embarked = ["C","S","Q"]
tdata = pd.read_csv("~/.kaggle/competitions/titanic/train.csv")
tdata["Title"] = tdata["Name"].str.split(" ").str.get(1)

def esp_cond_age(pclass, sex, sibsps, parchs, embarked, title) :
    filter = tdata[(tdata["Pclass"] == pclass) & (tdata["Sex"] == sex) & \
    (tdata["SibSp"] == sibsps) & (tdata["Parch"] == parchs) & \
    (tdata["Embarked"] == embarked) & (tdata["Title"] == title) & \
    (tdata["Age"].notnull())]
    if filter.count().PassengerId <= 1 :
        filter = tdata[(tdata["Pclass"] == pclass) & (tdata["Sex"] == sex) & \
        (tdata["SibSp"] == sibsps) & (tdata["Parch"] == parchs) & \
        (tdata["Embarked"] == embarked) & (tdata["Age"].notnull())]
    if filter.count().PassengerId <= 1 :
        filter = tdata[(tdata["Pclass"] == pclass) & (tdata["Sex"] == sex) & \
        (tdata["SibSp"] == sibsps) & (tdata["Parch"] == parchs) & \
        (tdata["Age"].notnull())]
    if filter.count().PassengerId <= 1 :
        filter = tdata[(tdata["Pclass"] == pclass) & (tdata["Sex"] == sex) & \
        (tdata["SibSp"] == sibsps) & (tdata["Age"].notnull())]
    if filter.count().PassengerId <= 1 :
        filter = tdata[(tdata["Pclass"] == pclass) & (tdata["Sex"] == sex) & \
        (tdata["Age"].notnull())]
    return filter['Age'].sum()/filter.count().PassengerId

ageArr = []
for index, row in tdata.iterrows() :
    if math.isnan(row["Age"]) :
        row["Age"] = esp_cond_age(row["Pclass"],row["Sex"],row["SibSp"], \
        row["Parch"],row["Embarked"],row["Title"])
    ageArr.append(row["Age"])
tdata["Age"] = np.array(ageArr)
tdata.to_csv('data_cleaned.csv')
print("DATA CLEANED")
