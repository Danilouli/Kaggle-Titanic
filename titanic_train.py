# | |                | |   | |  (_) |
# | |_ ___  __ _  ___| |__ | | ___| |_
# | __/ _ \/ _` |/ __| '_ \| |/ / | __|
# | ||  __/ (_| | (__| | | |   <| | |_
#  \__\___|\__,_|\___|_| |_|_|\_\_|\__|
# @Author: Daniel Saadia <danielsaadia>
# @Date:   2018-06-06T20:57:56+02:00
# @Email:  daniel@les-sherpas.co
# @Filename: titanic_train.py
# @Last modified by:   danielsaadia
# @Last modified time: 2018-06-06T21:10:48+02:00



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
{"lower" : 15, "higher" : 17},
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
{"lower" : 77, "higher" : 999},
]
sibsps = [0,1,2,3,4,5,6,7,8]
parchs = [0,1,2,3,4,5,6]
embarked = ["C","S","Q"]
tdata = pd.read_csv("~/.kaggle/competitions/titanic/train.csv")
tdata["FamilyName"] = tdata["Name"].str.split(",").str.get(0)
tdata["Title"] = tdata["Name"].str.split(" ").str.get(1)
for i in it.product(pclass, sex, ages, sibsps, parchs, embarked):
    print(i)
    print(i[2]["lower"])
    filter = tdata[(tdata["Pclass"] == i[0]) & (tdata["Sex"] == i[1]) & \
    (tdata["Age"] >= i[2]["lower"]) & (tdata["Age"] <= i[2]["higher"]) & (tdata["SibSp"] == i[3])\
    & (tdata["Parch"] == i[4]) & (tdata["Embarked"] == i[5])]
    nb = test.count()
    print(nb)
# print(test)
# print(nb)
# deads_classes = tdata[tdata["Survived"]==0]["Pclass"].value_counts()
# dataFrame = pd.DataFrame([survivors_classes, deads_classes])
# dataFrame.index = ["Survivors", "Deads"]
# print(dataFrame)
#
# perc1Surv = 100*(dataFrame.iloc[0,0]/dataFrame.iloc[:,0].sum())
# perc1Dead = 100 - perc1Surv
# perc2Surv = 100*(dataFrame.iloc[0,1]/dataFrame.iloc[:,1].sum())
# perc2Dead = 100 - perc2Surv
# perc3Surv = 100*(dataFrame.iloc[0,2]/dataFrame.iloc[:,2].sum())
# perc3Dead = 100 - perc3Surv
# surv_by_classes_df = pd.DataFrame([[perc1Surv, perc1Dead],[perc2Surv, perc2Dead],[perc3Surv, perc3Dead]])
# surv_by_classes_df.index = [1, 2, 3]
# surv_by_classes_df.columns = ["Live","Death"]
# print(surv_by_classes_df)
