# import inline
import matplotlib
import pip
import plotly
import seaborn
# from numpy.f2py.crackfortran import quiet


medical_charges_url =  'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
from urllib.request import urlretrieve
urlretrieve(medical_charges_url, 'medical.csv')
import pandas as pd
medical_df = pd.read_csv('medical.csv')
medical_df
medical_df.info()
medical_df.describe()
# !pip install jovian --quiet
# import jovian
# jovian.commit()

import plotly.express as px
import matplotlib
# %matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline



sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
fig = px.histogram(medical_df,
                   x='age',
                   marginal='box',
                   nbins=47,
                   title='Distribution of Age')
fig.update_layout(bargap=0.1)
fig.show()
plt.show()

medical_df.age.describe()
fig = px.histogram(medical_df, x = 'bmi',
                   marginal = 'box',
                   color_discrete_sequence= ['red'],
                   nbins = 47,
                   title='Distribution of BMI')
fig.update_layout(bargap=0.1)
fig.show()
plt.show()

fig = px.histogram(medical_df,
                   x='charges',
                   marginal='box',
                   color='smoker',
                   color_discrete_sequence=['green', 'grey'],
                   title='Annual Medical Charges')
fig.update_layout(bargap=0.1)
fig.show()
plt.show()
medical_df.smoker.value_counts()
px.histogram(medical_df, x ='smoker' , color = 'sex', title = 'Smoker')

fig = px.histogram(medical_df, x = 'sex' ,
                   marginal = 'box',
                  color = 'sex',
                   color_discrete_sequence= ['blue', 'pink'],
                   title='Gender')
fig.update_layout(bargap=0.1)
fig.show()
plt.show()

fig = px.scatter(medical_df,
                 x='age',
                 y = 'charges',
                 color = 'smoker',
                 opacity = 0.8,
                 hover_data=['sex'],
                 title='Age vs. Charges')
fig.update_traces(marker_size=5)
fig.show()
plt.show()

fig = px.scatter(medical_df,
                 x='bmi',
                 y='charges',
                 color='smoker',
                 opacity=0.8,
                 hover_data=['sex'],
                 title='BMI vs. Charges')
fig.update_traces(marker_size=5)
fig.show()
plt.show()
fig = px.violin(medical_df,
                x='age',
                y='charges',
                color='smoker',
                hover_data=['sex'],
                title='Age vs. Charges')
fig.update_traces(marker_size=5)
fig.show()

plt.show()

medical_df.chargs.corr(medical_df.age)
medical_df.chargs.corr(medical_df.charges)
smoker_values = {'no' : 0, 'yes' : 1}
smoker_numeric = medical_df.smoker.map(smoker_values)
medical_df.charges.corr(smoker_numeric)
sns.heatmap(medical_df.corr(), cmap='Reds', annot=True)
plt.title('Correlation Matrix')
non_smoker_df = medical_df[medical_df.smoker == 'no']
plt.title('age vs. Charges')
sns.scatterplot(data=non_smoker_df, x='age', y='charges', alpha= 0.7, s =15)
def estimate_charges(age,w,b):
     return w* age +b
w = 50
b = 100
ages = non_smoker_df.age
estimated_charges = estimate_charges(ages, w, b)
plt.plot(ages, estimated_charges, 'r-o')
plt.xlabel('Age')
plt.ylabel('Estimated Charges')
target = non_smoker_df.charges

plt.plot(ages, estimated_charges, 'r', alpha=0.9)
plt.scatter(ages, target, s=8,alpha=0.8)
plt.xlabel('Age')
plt.ylabel('Charges')
plt.legend(['Estimate', 'Actual'])


def try_parameters(w, b):
    ages = non_smoker_df.age
    target = non_smoker_df.charges

    estimated_charges = estimate_charges(ages, w, b)

    plt.plot(ages, estimated_charges, 'r', alpha=0.9)
    plt.scatter(ages, target, s=8, alpha=0.8)
    plt.xlabel('Age')
    plt.ylabel('Charges')
    plt.legend(['Estimate', 'Actual'])
    try_parameters(60, 200)
    try_parameters(400, 5000)
