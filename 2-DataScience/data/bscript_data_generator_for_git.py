# Git is now having a file limit by 25 MB.
# :-(
# @author: Dr. Benjamin M. Abdel-Karim
# @since: 2022-11-16
# @version: 2022-11-16
# @worktime: 5 min
import pandas as pd
import uuid

df = pd.read_csv('dataset_raw.csv')
df_sample = df.sample(frac=0.55)

# id and member_id are deleted by the data provider.
# For the dedicate approach this data a synthetic added.
# @code: [0:9] get only a few digits from the uuid as String .
for index, row in df_sample.iterrows():
    df_sample.loc[index, 'id'] = str(uuid.uuid1())[0:10]
    df_sample.loc[index, 'member_id'] = str(uuid.uuid1())[0:5]
print('// complete ....... id and member_id')

df_sample.to_csv('dataset_small.csv')
print('// complete ....... script')