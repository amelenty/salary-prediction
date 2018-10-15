import os
import pandas as pd
import pyramid.arima as pm

JOB_TITLES = ['Junior Software Engineer', 'Software Engineer', 'Senior Software Engineer']

all_data =pd.DataFrame(index=pd.date_range('20110601', '20180601', freq='6MS'))
data_files = os.listdir('data')
data_files.sort()
print(all_data)

def get_data_from_file(file):
    print('Processing ' + file)
    data = pd.read_csv('data/' + file)
    if ('Зарплата в месяц') in data.columns:
        salary_column_name = 'Зарплата в месяц'
    else:
        salary_column_name = 'Средняя зарплата в месяц'
    median_salaries = data.groupby(['Язык программирования', 'Должность']).median()[salary_column_name]
    return median_salaries

data_dict = {}

for file in data_files:
    data_dict[file[:-4]] = get_data_from_file(file)

all_data = pd.DataFrame.from_dict(data_dict, orient='index')
se_data = all_data.loc[:, (slice(None), JOB_TITLES)]
se_data = se_data.dropna(axis=1)

se_data.index = pd.to_datetime(se_data.index)

train, test = se_data.loc[:'2017-05', :], se_data.loc['2017-05':, :]

model_dict = {}
for column in train.columns:
    model_dict[column] = pm.auto_arima(train[column], start_p=1, start_q=1, max_p=3, max_q=3, m=2, start_P=0, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True, stepwise=True)
