import pandas as pd
import time
import warnings
import numpy as np
import random
import string
import seaborn as sns

df = pd.read_csv('features.csv')
print(df.columns)

def texture(texture):
    t = ['soft', 'silky', 'hard', 'matte', 'fluffy']
    for i in range(len(t)):
        if t[i] == texture:
            return i
    print('hello')
    return i

def genre(genre):
    t = ['rock', 'pop', 'jaaz', 'soft', 'metallic', 'romantic', 'folk', 'hiphop', 'mashups', 'cover']
    for i in range(len(t)):
        if t[i] == genre:
            return i
    print('hello')
    return i

def sports(sports):
    t = ['indoor', 'outdoor', 'virtual', 'augmented']
    for i in range(len(t)):
        if t[i] == sports:
            return i
    print('hello')
    return i

def ethnicity(ethnicity):
    t = ["Punjabi","Telugu","Marathi","Tamil","Hindi","Kannada","Bengali","Malayalam"]
    for i in range(len(t)):
        if t[i].lower() == ethnicity:
            return i
    print('hello')
    return i

def other_cities(other_cities):
    a = ["Hyderbad","Bangalore","Mumbai","Kolkata","Chennai","Jaipur","Delhi","Lucknow"]
    b = ["Chandigarh","Srinagar","Panaji","Jammu","Bhubaneswar","Chandigarh","Vijayawada"]
    c = ["Itanagar","Dispur","Patna","Raipur","Gandhinagar","Shimla","Ranchi"]
    d = ["Thiruvananthapuram","Bhopal", "Imphal","Shillong","Aizawl","Kohima","Gangtok","Agartala","Dehradun"]
    if other_cities in a:
        return 0
    elif other_cities in b:
        return 1
    elif other_cities in c:
        return 2
    else:
        return 3
    print('hello')
    return 1

def fav_color(fav_color):
    t = ["red", "pink", "orange", "yellow", "purple", "green", "blue", "brown", "white", "grey", "black"]
    for i in range(len(t)):
        if t[i].lower() == fav_color:
            return i
    print('hello')
    return i

def hobbies(hobbies):
    t = ['sports', 'reading', 'watching', 'cooking', 'volunteering', 'dancing', 'singing', 'sleeping', 'traveling', 'acting']
    for i in range(len(t)):
        if t[i].lower() == hobbies:
            return i
    print('hello')
    return i



df['texture'] = df['texture'].apply(lambda x: texture(x))
df['genre'] = df['genre'].apply(lambda x: genre(x))
df['sports'] = df['sports'].apply(lambda x: sports(x))
df['ethnicity'] = df['ethnicity'].apply(lambda x: ethnicity(x))
df['other_cities'] = df['other_cities'].apply(lambda x: other_cities(x))
df['fav_color'] = df['fav_color'].apply(lambda x: fav_color(x))
df['hobbies'] = df['hobbies'].apply(lambda x: hobbies(x))

df.to_csv("final_features.csv", index=False)