import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

Test = pd.read_csv("http://bit.ly/HDSC-Dataset")
print(Test.describe())
Test.groupby('Fuel_type_code_pudl')
print(Test.groupby('Fuel_type_code_pudl').mean())
