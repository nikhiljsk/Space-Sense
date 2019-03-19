import pandas as pd
import time
import warnings
import numpy as np
import random
import string

warnings.filterwarnings("ignore")
start = time.clock()


marital = ['married'] * 55 + ['unmarried'] * 25 + ['widow'] * 7 + ['divorced'] * 13
age = np.random.randint(5, 19, size=(1, 25)).tolist()[0]  + np.random.randint(18, 31, size=(1, 40)).tolist()[0] +  np.random.randint(30, 61, size=(1, 40)).tolist()[0] + np.random.randint(60, 80, size=(1, 5)).tolist()[0]  
gender = ['male'] * 55 + ['female'] * 40 + ['unspecified'] * 5
rooms = [1]*25 + [2]*30 + [3]*30 + [4]*5
hobbies = ['sports', 'reading', 'watching', 'cooking', 'volunteering', 'dancing', 'singing', 'sleeping', 'traveling', 'acting'] * 10
alcoholic = ['yes', 'no'] * 50
income = np.random.randint(100000, 1000000, size=(1, 50)).tolist()[0]  + np.random.randint(1000000, 6000000, size=(1, 30)).tolist()[0] +  np.random.randint(6000000, 10000000, size=(1, 20)).tolist()[0]
color = ["red"] * 9 + ["pink"] * 9 + ["orange"] * 9 + ["yellow"] * 9 + ["purple"] * 9 + ["green"] * 9 + ["blue"] * 9 + ["brown"] * 9 + ["white"] * 9 + ["grey"] * 9 +["black"] * 10
other = np.random.randint(1, 3, size=(1, 60)).tolist()[0]  + np.random.randint(2, 5, size=(1, 30)).tolist()[0] +  np.random.randint(4, 9, size=(1, 7)).tolist()[0] + np.random.randint(8, 11, size=(1, 3)).tolist()[0]  
work = np.random.randint(0, 5, size=(1, 10)).tolist()[0]  + np.random.randint(4, 9, size=(1, 40)).tolist()[0] +  np.random.randint(8, 11, size=(1, 40)).tolist()[0] + np.random.randint(10, 13, size=(1, 20)).tolist()[0]  
energy = np.random.randint(250, 1000, size=(1, 30)).tolist()[0]  + np.random.randint(1000, 2000, size=(1, 25)).tolist()[0] +  np.random.randint(2000, 3000, size=(1, 20)).tolist()[0] + np.random.randint(3000,4000, size=(1, 10)).tolist()[0]  
genre = ['rock', 'pop', 'jaaz', 'soft', 'metallic', 'romantic', 'folk', 'hiphop', 'mashups', 'cover'] * 10
high = ['yes', 'no'] * 50
nature = ['yes', 'no'] * 50
devotional = ['yes'] * 70 + ['no'] * 30
outing = ['yes', 'no', 'not so often'] * 33 + ['yes']
texture = ['soft', 'silky', 'hard', 'matte', 'fluffy'] * 20
distance = np.random.randint(1, 11, size=(1, 60)).tolist()[0]  + np.random.randint(10, 16, size=(1, 20)).tolist()[0] +  np.random.randint(15, 21, size=(1, 10)).tolist()[0] + np.random.randint(20, 31, size=(1, 10)).tolist()[0]  
sports = ['indoor', 'outdoor', 'virtual', 'augmented'] * 25
expenses = np.random.randint(1, 11, size=(1, 35)).tolist()[0]  + np.random.randint(10, 21, size=(1, 30)).tolist()[0] +  np.random.randint(20, 31, size=(1, 25)).tolist()[0] + np.random.randint(30, 41, size=(1, 10)).tolist()[0]  
cities = np.random.randint(1, 4, size=(1, 100)).tolist()[0]
education = np.random.randint(0, 13, size=(1, 20)).tolist()[0]  + np.random.randint(12, 15, size=(1, 25)).tolist()[0] +  np.random.randint(14, 19, size=(1, 25)).tolist()[0] + np.random.randint(18, 25, size=(1,10)).tolist()[0]
ethnicity = ["Punjabi","Telugu","Marathi","Tamil","Hindi","Kannada","Bengali","Malayalam"] * 12 + ["Telugu", "Punjabi"]  * 2 

n = 10000

data = {
       "marital status": [random.choice(marital).lower() for x in range(n)],
       "age": [random.choice(age) for x in range(n)],
       "gender": [random.choice(gender).lower() for x in range(n)],
       "rooms": [random.choice(rooms) for x in range(n)],
       "hobbies": [random.choice(hobbies).lower() for x in range(n)],
       "alcoholic": [random.choice(alcoholic).lower() for x in range(n)],
       "annual_income": [random.choice(income) for x in range(n)],
       "fav_color": [random.choice(color).lower() for x in range(n)],
       "other_props": [random.choice(other) for x in range(n)],
       "work_hours": [random.choice(work) for x in range(n)],
       "avg_energy": [random.choice(energy) for x in range(n)],
       "other_cities": [random.choice(cities).lower() for x in range(n)],
       "office_distance": [random.choice(distance) for x in range(n)],
       "ethnicity": [random.choice(ethnicity).lower() for x in range(n)],
       "devotional": [random.choice(devotional).lower() for x in range(n)],
       "ed_qualification": [random.choice(education) for x in range(n)],
       "expenses": [random.choice(expenses) for x in range(n)],
       "genre": [random.choice(genre).lower() for x in range(n)],
       "nature_lover": [random.choice(nature).lower() for x in range(n)],
       "high_raise_apt": [random.choice(high).lower() for x in range(n)],
       "sports": [random.choice(sports).lower() for x in range(n)],
       "texture": [random.choice(texture).lower() for x in range(n)],
       "outing": [random.choice(outing).lower() for x in range(n)],
     }
df = pd.DataFrame(data)

def marital_age(marital, age):
    if age < 21 and marital == 'yes':
        return 'no'
    return marital

def income_expense(income, expenses):
    if income <= expenses:
        while(income > expenses):
            expenses *= 0.9
        return expenses
    return expenses

# Re-check data

df['marital status'] = df.apply(lambda row: marital_age(row['marital status'], row['age']), axis=1)
df['expenses'] = df.apply(lambda row: income_expense(row['annual_income'], row['expenses']), axis=1)
   
end = time.clock()
print("The process took", end-start, "seconds")


print("Generated", n, " records! [personality_survery.csv]")
df.to_csv("personality_survery.csv", encoding='utf-8', index=False)


l = [random.choice(gender) for x in range(n)]