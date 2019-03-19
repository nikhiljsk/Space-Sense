import pandas as pd
df = pd.read_csv('final_features.csv')
def call(x):
    return np.random.randint(1, 4)
df['other_cities'] = df['other_cities'].apply(lambda x: call(x))
df.to_csv('final_features.csv', index=False)