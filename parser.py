import os
import pandas as pd

data_files = os.listdir('data')

for file in data_files:
    print('Processing ' + file)
    data = pd.read_csv(file)
    median_salaries = data.groupby(['Язык программирования', 'Должность']).median()['Средняя зарплата в месяц']
