import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
import sklearn.linear_model

## @AUTHOR: TREVOR KNOTT
## @EMAIL: tk@trevorknott.io
## @REFERENCE: Using Reference`Hands on Machine Learning ... By: O`Reily Books

## @ABOUT Linear Model Training using Scikit-Learn




# Step (1) Load the data
oecd_bli = pd.read_csv("../Data/SectionONE_Data/oecd_bli_2015.csv", thousands=',')
gdp_per_capita = pd.read_csv("../Data/SectionONE_Data/gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin1', na_values="n/a")


# Step (2) Make Prepare Prep Method
def prepare_country_stats(oecd_bli, gdp_per_capita):
    #get the pandas dataframe of GDP per capita and Life satisfaction
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita, left_index=True, right_index=True)
    return full_country_stats[["GDP per capita", 'Life satisfaction']]


# Step (3) Prepare the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]


# Step (4) Visualize the Data
country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')
country_stats.to_csv('../Data/SectionONE_Data/prepared_after_train/LinModelNORegLine_country_stats.csv',encoding='utf-8')

plt.show()

# Step (5) Select a Linear Model
model = sklearn.linear_model.LinearRegression()

# Step (6) Train the Model
model.fit(X, y)

# Step (7) Make prediction for cyprus
X_new=[[22587]]
print(model.predict(X_new))


