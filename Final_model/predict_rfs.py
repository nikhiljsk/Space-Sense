import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
import _pickle as cPickle
#Ignoring warnings
import warnings
warnings.filterwarnings("ignore")
from PIL import Image,ImageDraw , ImageFont
import sys


def report(data):
    image = Image.open("images/"+data[3]+"_image.png")
    coordinates= [[140,460],[675,630],[158,990],[662,1220],[162,1470]]
    draw = ImageDraw.Draw(image)
    font_2 = ImageFont.truetype("arial.ttf", 30)
    for i in range(5):
        draw.text(xy= coordinates[i],text = data[i] ,fill = "#FFFFFF", font = font_2)
    image.save("report.png")



with open('model_rfr', 'rb') as f:
    lm6 = cPickle.load(f)


json1_file = open("1.json")
json1_str = json1_file.read()
to_pred = json.loads(json1_str)

def change_data(data):
    co = ["red", "pink", "orange", "yellow", "purple", "green", "blue", "brown", "white", "grey", "black"]
    ge = ["male", "female", "unspecified"]
    genr = ['rock', 'pop', 'jaaz', 'soft', 'metallic', 'romantic', 'folk', 'hiphop', 'mashups', 'cover']
    hob = ['sports', 'reading', 'watching', 'cooking', 'volunteering', 'dancing', 'singing', 'sleeping', 'traveling', 'acting']
    mar = ['married' ,'unmarried', 'divorced', 'widow']
    out = ["no", "yes", "not so often"]
    sp = ['indoor', 'outdoor', 'virtual', 'augmented']
    tex = ['soft', 'silky', 'hard', 'matte', 'fluffy']
    
    data["age"] = int(data["age"])
    data["alcoholic"] = 1 if data["alcoholic"]=="yes" else 0
    data["devotional"] = 1 if data["devotional"]=="yes" else 0
    data["avg_energy"] = int(data["avg_energy"])
    data["annual_income"] = int(data["annual_income"])
    data["ed_qualification"] = int(data["ed_qualification"])
    data["expenses"] = int(data["expenses"])
    data["fav_color"] = co.index(data["fav_color"])
    data["gender"] = ge.index(data["gender"])
    data["genre"] = genr.index(data["genre"])
    data["high_raise_apt"] = 1 if data["high_raise_apt"]=="yes" else 0
    data["hobbies"] = hob.index(data["hobbies"])
    data["marital_status"] = mar.index(data["marital_status"])
    data["nature_lover"] = 1 if data["nature_lover"]=="yes" else 0
    data["office_distance"] = int(data["office_distance"])
    data["other_cities"] = int(data["other_cities"])
    data["other_props"] = int(data["other_props"])
    data["outing"] = out.index(data["outing"])
    data["rooms"] = int(data["rooms"])
    data["sports"] = sp.index(data["sports"])
    data["texture"] = tex.index(data["texture"])
    data["work_hours"] = int(data["work_hours"])

    return data
to_pred = change_data(to_pred)


cluster = lm6.predict([[to_pred['marital_status'],to_pred['age'],to_pred['gender'],to_pred['rooms'],to_pred['hobbies'],to_pred['alcoholic'],to_pred['annual_income'],to_pred['fav_color'],to_pred['other_props'],to_pred['work_hours'],to_pred['avg_energy'],to_pred['other_cities'],to_pred['office_distance'],to_pred['devotional'],to_pred['ed_qualification'],to_pred['expenses'],to_pred['genre'],to_pred['nature_lover'],to_pred['high_raise_apt'],to_pred['sports'],to_pred['texture'],to_pred['outing']]])
cluster = int(round(cluster[0],0))
#print(cluster)
score = (to_pred['rooms'])+(to_pred['alcoholic'])+(to_pred['annual_income']//1000000)+(to_pred['other_props'])+(to_pred['expenses']/1000)+to_pred['other_cities'] 
#print(score)
cost = score * 250000
if 0 <= score <= 7:
    c_type = "peaceful"
elif 7 < score < 9:
    c_type = "adventurous"
elif 9 <= score < 14:
    c_type = "jazzy"
elif 14 <= score < 16:
    c_type = "rich"
else:
    c_type = "royal"
    
marital = to_pred['marital_status']
age = to_pred['age']
rooms = to_pred['rooms']

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


    
if cluster == 1:
    data = ["hustle", str(int(size_of_family)), c_type, "funky", str(int(cost))]
    report(data)
elif cluster == 2:
    data = ["hustle", str(int(size_of_family)), c_type, "charming", str(int(cost))]
    report(data)
elif cluster == 3:
    data = ["ponderous",  str(int(size_of_family)), c_type, "cool", str(int(cost))]
    report(data)
elif cluster == 4:
    data = ["exploring", str(int(size_of_family)), c_type, "loving", str(int(cost))]
    report(data)
elif cluster == 5:
    data = ["ponderous", str(int(size_of_family)), c_type, "cool", str(int(cost))]
    report(data)
elif cluster == 6:
    data = ["exploring",  str(int(size_of_family)), c_type, "funky", str(int(cost))]
    report(data)
elif cluster == 7:
    data = ["exploring", str(int(size_of_family)), c_type, "loving", str(int(cost))]
    report(data)
elif cluster == 8:
    data = ["ponderous", str(int(size_of_family)), c_type, "cool", str(int(cost))]
    report(data)
elif cluster == 9:
    data = ["hustle", str(int(size_of_family)), c_type, "funky", str(int(cost))]
    report(data)
elif cluster == 10:
    data = ["ponderous", str(int(size_of_family)), c_type, "charming", str(int(cost))]
    report(data)


predict_data ={}
predict_data["State_of_Mind"] = data[0]
predict_data["Family_Count"] = data[1]
predict_data["Lifestyle"] = data[2]
predict_data["Mood"]  = data[3]
predict_data["Estimated Budget"] = data [4]
predict_data["cluster"] = str(cluster)
print(predict_data)

cluster_outputs = {}
cluster_outputs["cluster"] = str(cluster)

with open( "customer_data.txt", 'w') as datawriter:
    datawriter.write(json1_str)
    datawriter.write(json.dumps(predict_data))
    datawriter.write(json.dumps(cluster))

print("\n\n", json1_str)

#display(predictions_rfr, y_test, "Random Forest Regression")
#report(data)
    
