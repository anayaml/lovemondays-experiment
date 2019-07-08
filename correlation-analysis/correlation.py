import pandas as pd

dataframe = pd.read_csv('lovemondays_turnover.csv')

print(dataframe.corr(method='pearson'))