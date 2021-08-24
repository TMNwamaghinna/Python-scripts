import pandas as pd
import numpy as np

Homework = pd.read_csv('Hamoye.csv')
print(Homework.describe())

print(Homework.isnull())

print(Homework.groupby("fuel_type_code_pudl").mean())
