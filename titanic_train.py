import numpy as np
import pandas as pd
import itertools as it


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
tdata = pd.read_csv("data_cleaned.csv")
res = np.ndarray(shape=(4,2,101,101,9,7,3))
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

for i in it.product(pclass, sex, ages, sibsps, parchs, embarked):
    filter = tdata[(tdata["Pclass"] == i[0]) & (tdata["Sex"] == i[1]) & \
    (tdata["Age"] >= i[2]["lower"]) & (tdata["Age"] <= i[2]["higher"]) & (tdata["SibSp"] == i[3]) & \
    (tdata["Parch"] == i[4]) & (tdata["Embarked"] == str(i[5]))]
    filterSurv = tdata[(tdata["Survived"] == 1) & (tdata["Pclass"] == i[0]) & (tdata["Sex"] == i[1]) & \
    (tdata["Age"] >= i[2]["lower"]) & (tdata["Age"] <= i[2]["higher"]) & (tdata["SibSp"] == i[3]) & \
    (tdata["Parch"] == i[4]) & (tdata["Embarked"] == str(i[5]))]
    if filter.count().PassengerId == 0 :
        filter = tdata[(tdata["Pclass"] == i[0]) & (tdata["Sex"] == i[1]) & \
        (tdata["Age"] >= i[2]["lower"]) & (tdata["Age"] <= i[2]["higher"]) & (tdata["SibSp"] == i[3]) & \
        (tdata["Parch"] == i[4])]
        filterSurv = tdata[(tdata["Survived"] == 1) & (tdata["Pclass"] == i[0]) & (tdata["Sex"] == i[1]) & \
        (tdata["Age"] >= i[2]["lower"]) & (tdata["Age"] <= i[2]["higher"]) & (tdata["SibSp"] == i[3]) & \
        (tdata["Parch"] == i[4])]
    if filter.count().PassengerId == 0 :
        filter = tdata[(tdata["Pclass"] == i[0]) & (tdata["Sex"] == i[1]) & \
        (tdata["Age"] >= i[2]["lower"]) & (tdata["Age"] <= i[2]["higher"]) & (tdata["SibSp"] == i[3])]
        filterSurv = tdata[(tdata["Survived"] == 1) & (tdata["Pclass"] == i[0]) & (tdata["Sex"] == i[1]) & \
        (tdata["Age"] >= i[2]["lower"]) & (tdata["Age"] <= i[2]["higher"]) & (tdata["SibSp"] == i[3])]
    if filter.count().PassengerId == 0 :
        filter = tdata[(tdata["Pclass"] == i[0]) & (tdata["Sex"] == i[1]) & \
        (tdata["Age"] >= i[2]["lower"]) & (tdata["Age"] <= i[2]["higher"])]
        filterSurv = tdata[(tdata["Survived"] == 1) & (tdata["Pclass"] == i[0]) & (tdata["Sex"] == i[1]) & \
        (tdata["Age"] >= i[2]["lower"]) & (tdata["Age"] <= i[2]["higher"])]
    if filter.count().PassengerId == 0 :
        filter = tdata[(tdata["Pclass"] == i[0]) & (tdata["Sex"] == i[1])]
        filterSurv = tdata[(tdata["Survived"] == 1) & (tdata["Pclass"] == i[0]) & (tdata["Sex"] == i[1])]
    nb = filter.count().PassengerId
    nbSurv = filterSurv.count().PassengerId
    if nb > 0 :
        result = nbSurv/nb
        print("PROB FOR : pclass " + str(i[0]) + ", sex : " + i[1] + ", age : " + str(i[2]) + ", sibsp : " + str(i[3]) + \
        ", parch : " + str(i[4]) + ", embarked : " + str(i[5]) + " = " + str(result))
        res[i[0]][dtn("Sex",i[1])][i[2]["lower"]][i[2]["higher"]][i[3]][i[4]][dtn("Embarked",i[5])] = result
    else:
        res[i[0]][dtn("Sex",i[1])][i[2]["lower"]][i[2]["higher"]][i[3]][i[4]][dtn("Embarked",i[5])] = -1
        print("NEGPROB FOR : pclass " + str(i[0]) + ", sex : " + i[1] + ", age : " + str(i[2]) + ", sibsp : " + str(i[3]) + \
        ", parch : " + str(i[4]) + ", embarked : " + str(i[5]) + " = " + str(result))

def prob(pclass, sex, lowerAge, higherAge, sibsp, parch, embarked) :
    return (res[pclass][dtn("Sex",sex)][lowerAge][higherAge][sibsp][parch][dtn("Embarked",embarked)])

np.save('results.npy', res)
print("RESULTS.NPY FILE FILLED")
