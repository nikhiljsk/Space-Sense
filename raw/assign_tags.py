import pandas as pd
import time
import warnings
import numpy as np
import random
import string
import seaborn as sns

df = pd.read_csv('personality_survery.csv')

def classify(marital, age, gender, rooms, alcoholic, annual_income, other_props, expenses, other_cities):
    # size of family
    if marital == "married" and 18 <= age <= 60 and 0<=rooms<=2:
        size_of_family = 4
    elif marital == "married" and 60 <= age <= 100:
        size_of_family = 3
    elif marital == "married" and 18 <= age <= 60 and 2<=rooms<=4:
        size_of_family = 7
    elif marital == "unmarried" and 18 <= age <= 60 and 0<=rooms<=2:
        size_of_family = 3
    elif marital == "unmarried" and 18 <= age <= 60 and 2<=rooms<=4:
        size_of_family = 5
    elif marital == "unmarried" and 0 <= age <= 18 and 0<=rooms<=2:
        size_of_family = 3
    elif marital == "unmarried" and 17 <= age <= 24 and 0<=rooms<=2:
        size_of_family = 1
    elif marital == "unmarried" and 18 <= age <= 60 and 0<=rooms<=2:
        size_of_family = 2
    else:
        size_of_family = 4
        
    # age groups
    if 0 <= age <= 18:
        g_type = 1          # child 
    elif 18 < age <= 25:
        g_type = 2          #teenage
    elif 25 <= age <= 50:
        g_type = 3          # elder
    else:
        g_type = 4          # older
    
    # class
    al = 1 if alcoholic == "yes" else 0
    income = int(annual_income)//1000000
    expenses /= 1000
    score = (rooms)+(al)+(income)+(other_props)+(expenses)+int(2) # other_cities
    
    if 0 <= score <= 7:
        c_type = 5
    elif 7 < score < 9:
        c_type = 4
    elif 9 <= score < 14:
        c_type = 3
    elif 14 <= score < 16:
        c_type = 2
    else:
        c_type = 1
    
    # group 1
    if marital == "unmarried" and gender == "male" and g_type == 2:
        cluster = 1
    elif marital == "unmarried" and gender == "female" and g_type == 2:
        cluster = 2
    elif marital == "married" and c_type == 1:
        cluster = 3
    elif marital == "married" and c_type == 3 or c_type == 2 :
        cluster = 4
    elif marital == "married" and c_type == 4 and g_type == 4:
        cluster = 5
    elif marital == "unmarried" and c_type == 2 or c_type == 3:
        cluster = 6
    elif marital == "unmarried" and g_type == 1:
        cluster = 7
    elif (marital == "divorced" or marital == "widow"):
        cluster = 8
    elif marital == "married" and g_type == 3 or c_type == 4 or gender == "female":
        cluster = 9
    elif marital == "married" and g_type == 3 or c_type == 4 or gender == "male":
        cluster = 10
    else:
        cluster = random.randint(1, 10)
        
        
    return cluster


df['group'] = df.apply(lambda row: classify(row['marital status'], row['age'], row['gender'], row['rooms'], row['alcoholic'], row['annual_income'], row['other_props'], row['expenses'], row['other_cities']), axis=1)

df.to_csv("features.csv", index=False)

sns.distplot(df["group"])