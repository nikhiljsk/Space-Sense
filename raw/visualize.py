import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = pd.read_csv("personality_survery.csv")
#sns.distplot(data["age"],bins=5)

#sns.distplot(data["rooms"],bins =5)
#sns.plt.ylim(0,4)
#sns.plt.xlim(0,4)


#sns.distplot(data["other_props"],bins =5)

#sns.distplot(data["work_hours"],bins =5)

#sns.distplot(data["avg_energy"],bins =5)
#sns.distplot(data["office_distance"],bins =5)

#sns.distplot(data["ed_qualification"],bins =5)

sns.distplot(data["expenses"],bins =5)


plt.show()