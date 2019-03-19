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


json1_file = open("1.json")
json1_str = json1_file.read()
to_pred = json.loads(json1_str)

									# Part - 2 Algorithm

# Data-Preprocessing
data = pd.read_csv('final_features.csv')
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Spliting Data 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


#Random Forest
from sklearn.ensemble import RandomForestRegressor
lm6 = RandomForestRegressor(n_estimators=1000)
lm6.fit(X_train, y_train)
predictions_rfr = lm6.predict(X_test)
predictions_rfr = np.reshape(predictions_rfr, (3000, ))


with open('model_rfr', 'wb') as f:
    cPickle.dump(lm6, f)