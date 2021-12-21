import numpy as np
import pandas as pd
# uiks = pd.read_csv('data/cities.csv', index_col=0)
# cityt = pd.read_excel('data/cityt.xlsx')
# uikseng = pd.DataFrame()
#
# for city in uiks['city300'].drop_duplicates():
#     theregion = cityt[cityt['Город'] == city]
#     if len(theregion) == 0:
#         print(city)
#     change = uiks[uiks['city300'] == city]
#     change['city300'] = theregion['City'].iloc[0]
#     uikseng = uikseng.append(change)


uiks = pd.read_csv('data/edata_eng.csv', index_col=0)