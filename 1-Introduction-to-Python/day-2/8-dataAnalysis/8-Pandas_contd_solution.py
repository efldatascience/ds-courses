import pandas as pd



# %%
#create dummy DataFrames
Ddata1 = {
        'id': ['1', '2', '3', '4', '5'],
        'Feature1': ['A', 'C', 'E', 'G', 'I'],
        'Feature2': ['B', 'D', 'F', 'H', 'J']}

Ddata2 = {
        'id': ['1', '2', '6', '7', '8'],
        'Feature1': ['K', 'M', 'O', 'Q', 'S'],
        'Feature2': ['L', 'N', 'P', 'R', 'T']}

Ddata3 = {
        'id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'Feature3': [12, 13, 14, 15, 16, 17, 15, 12, 13, 23]}


df1 = pd.DataFrame(Ddata1, columns = ['id', 'Feature1', 'Feature2'])
df2 = pd.DataFrame(Ddata2, columns = ['id', 'Feature1', 'Feature2'])
df3 = pd.DataFrame(Ddata3, columns = ['id', 'Feature3'])




# %%
"""
concatenation
"""

#concatenate two DataFrames along the row
df_row = pd.concat([df1, df2])




# %%
#concatenate two DataFrames along the row, ignore_index = True
df_row = pd.concat([df1, df2], ignore_index = True)




# %%
#concatenate two DataFrames along the row using labels for each DataFrame
df_keys = pd.concat([df1, df2], keys = ['df1', 'df2'])

#get data from df2 of the new DataFrame
print(df_keys.loc['df2'])




# %%
#concatenate two DataFrames along the column
df_col = pd.concat([df1, df2], axis = 1)





# %%
"""
merge
"""

#different merge operations
left = pd.DataFrame({'key': ['K0', 'K2', 'K3'],
                     'A': ['A0', 'A2', 'A3'],
                     'B': ['B0', 'B2', 'B3']})


right = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']})

#merge two dataframes based on a common column
result_inner = pd.merge(left, right, on='key')




result_outer = pd.merge(left, right, on='key', how = 'outer')
result_left = pd.merge(left, right, on='key', how = 'left')
result_right = pd.merge(left, right, on='key', how = 'right')



df_merge_col = pd.merge(df_row, df3, on='id')




# %%
#merge two dataframes with different names for the common column

left = pd.DataFrame({'key': ['K0', 'K2', 'K3'],
                     'A': ['A0', 'A2', 'A3'],
                     'B': ['B0', 'B2', 'B3']})


right = pd.DataFrame({'id': ['K0', 'K1', 'K2'],
                      'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']})

df_merge_difkey = pd.merge(left, right, left_on='key', right_on='id')




# %%
#merge two dataframes with multiple keys

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                 'key2': ['K0', 'K1', 'K0', 'K1'],
                 'A': ['A0', 'A1', 'A2', 'A3'],
                 'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                     'key2': ['K0', 'K0', 'K0', 'K0'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})

df_merge_multkey = pd.merge(left, right, on=['key1', 'key2'], how='outer')



