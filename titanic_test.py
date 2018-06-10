import numpy as np
import pandas as pd
import math
import random
from random import randint


cldata = pd.read_csv("data_cleaned.csv")
tsdata = pd.read_csv("~/.kaggle/competitions/titanic/test.csv")
model = np.load("results.npy")
tsdata["Title"] = tsdata["Name"].str.split(" ").str.get(1)

def esp_cond_age_t(pclass, sex, sibsps, parchs, embarked, title) :
    filter = cldata[(cldata["Pclass"] == pclass) & (cldata["Sex"] == sex) & \
    (cldata["SibSp"] == sibsps) & (cldata["Parch"] == parchs) & \
    (cldata["Embarked"] == embarked) & (cldata["Title"] == title) & \
    (cldata["Age"].notnull())]
    tFilter = tsdata[(tsdata["Pclass"] == pclass) & (tsdata["Sex"] == sex) & \
    (tsdata["SibSp"] == sibsps) & (tsdata["Parch"] == parchs) & \
    (tsdata["Embarked"] == embarked) & (tsdata["Title"] == title) & \
    (tsdata["Age"].notnull())]
    if filter.count().PassengerId + tFilter.count().PassengerId == 0 :
        filter = cldata[(cldata["Pclass"] == pclass) & (cldata["Sex"] == sex) & \
        (cldata["SibSp"] == sibsps) & (cldata["Parch"] == parchs) & \
        (cldata["Embarked"] == embarked) & \
        (cldata["Age"].notnull())]
        tFilter = tsdata[(tsdata["Pclass"] == pclass) & (tsdata["Sex"] == sex) & \
        (tsdata["SibSp"] == sibsps) & (tsdata["Parch"] == parchs) & \
        (tsdata["Embarked"] == embarked) & \
        (tsdata["Age"].notnull())]
    if filter.count().PassengerId + tFilter.count().PassengerId == 0 :
        filter = cldata[(cldata["Pclass"] == pclass) & (cldata["Sex"] == sex) & \
        (cldata["SibSp"] == sibsps) & (cldata["Parch"] == parchs) & \
        (cldata["Age"].notnull())]
        tFilter = tsdata[(tsdata["Pclass"] == pclass) & (tsdata["Sex"] == sex) & \
        (tsdata["SibSp"] == sibsps) & (tsdata["Parch"] == parchs) & \
        (tsdata["Age"].notnull())]
    if filter.count().PassengerId + tFilter.count().PassengerId == 0 :
        filter = cldata[(cldata["Pclass"] == pclass) & (cldata["Sex"] == sex) & \
        (cldata["SibSp"] == sibsps) & \
        (cldata["Age"].notnull())]
        tFilter = tsdata[(tsdata["Pclass"] == pclass) & (tsdata["Sex"] == sex) & \
        (tsdata["SibSp"] == sibsps) & \
        (tsdata["Age"].notnull())]
    if filter.count().PassengerId + tFilter.count().PassengerId == 0 :
        filter = cldata[(cldata["Pclass"] == pclass) & (cldata["Sex"] == sex) & \
        (cldata["Age"].notnull())]
        tFilter = tsdata[(tsdata["Pclass"] == pclass) & (tsdata["Sex"] == sex) & \
        (tsdata["Age"].notnull())]
    num = filter['Age'].sum() + tFilter['Age'].sum()
    den = filter.count().PassengerId + tFilter.count().PassengerId
    return num/den

ageArr = []
for index, row in tsdata.iterrows() :
    if math.isnan(row["Age"]) :
        row["Age"] = esp_cond_age_t(row["Pclass"],row["Sex"],row["SibSp"], \
        row["Parch"],row["Embarked"],row["Title"])
    ageArr.append(row["Age"])
tsdata["Age"] = np.array(ageArr)
tsdata.to_csv('test_cleaned.csv')

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

def iround(x):
    return int(round(x) - .5) + (x > 0)

def dtn(data, value) :
    if data == "Sex":
        if value == "male":
            return (0)
        else:
            return (1)
    if data == "Embarked":
        if value == "C":
            return (0)
        if value == "S":
            return (1)
        if value == "Q":
            return (2)

def age_placer(age) :
    if math.isnan(age) :
        print("RANDOOOOM AGE")
        age = randint(10, 50)
    age = iround(age)
    for a in ages :
        if (a["lower"] <= age) & (age <= a["higher"]) :
            return a

def prob(pclass, sex, lowerAge, higherAge, sibsp, parch, embarked) :
    return (model[pclass][dtn("Sex",sex)][lowerAge][higherAge][sibsp][parch][dtn("Embarked",embarked)])

retdf = pd.DataFrame(columns=["PassengerId","Survived"])
for index, row in tsdata.iterrows() :
    ageO = age_placer(row["Age"])
    if row["SibSp"] >= 8 :
        row["SibSp"] = 8
    if row["Parch"] >= 6 :
        row["Parch"] = 6
    proba = prob(row["Pclass"],row["Sex"],ageO["lower"],ageO["higher"],row["SibSp"],row["Parch"],row["Embarked"])
    # chance = random.uniform(0,1)
    # if chance <= proba :
    #     survived = 1
    # else :
    #     survived = 0
    if proba > 0.5 :
        survived = 1
    else :
        survived = 0
    if proba == -1 :
        print("RANDOOOOM PROB")
        survived = randint(0,1)
    retdf.loc[index] = [0,0]
    retdf.loc[index]["PassengerId"] = row["PassengerId"]
    retdf.loc[index]["Survived"] = survived
    # print("PROB FOR ID : " + str(row["PassengerId"]) + "")
retdf.to_csv('submission.csv')
print("SUMISSION DONE")
print(retdf)
