#%% Load data

import pandas as pd
stations = pd.read_csv('data/edata_eng.csv', index_col=0)

#%% Load data

stations = stations[stations['total_voters']>100]
stations = stations[stations['total_voters']<10000]
stations = stations[stations['ur']>5]
len(stations)

#%% Result vs Turnout for all Russia

import matplotlib.pyplot as plt
stations['ur_percent'] = stations['ur'] / (stations['voted'])
stations['cprf_percent'] = stations['cprf'] / (stations['voted'])
er_string = str(round(100*stations['ur'].sum()/stations['voted'].sum(),2)) + '%'
cprf_string = str(round(100*stations['cprf'].sum()/stations['voted'].sum(),2))+ '%'
stations['turnout'] = stations['voted']/stations['total_voters']
plt.scatter(stations['turnout'], stations['ur_percent'], color='blue', s=0.05, label="United Russia " + er_string)
plt.scatter(stations['turnout'], stations['cprf_percent'], color='red', s=0.05, label="CPRF " + cprf_string)
lgnd = plt.legend(loc="upper left", scatterpoints=1, fontsize=10)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
plt.xlabel("turnout")
plt.ylabel("party result")
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()

#%% Number of selected voted stations in cities:

city_stations = pd.read_csv('data/cities_ok_eng.csv', index_col=0)
city_stations['total_voters'].sum()
len(stations)

#%% Number of voters:

city_stations['total_voters'].sum()

#%% Result vs Turnout

import matplotlib.pyplot as plt
city_stations['ur_percent'] = city_stations['ur'] / (city_stations['voted'])
city_stations['cprf_percent'] = city_stations['cprf'] / (city_stations['voted'])
er_string = str(round(100*city_stations['ur'].sum()/city_stations['voted'].sum(),2)) + '%'
cprf_string = str(round(100*city_stations['cprf'].sum()/city_stations['voted'].sum(),2))+ '%'
city_stations['turnout'] = city_stations['voted']/city_stations['total_voters']
plt.scatter(city_stations['turnout'], city_stations['ur_percent'], color='blue', s=0.05, label="United Russia " + er_string)
plt.scatter(city_stations['turnout'], city_stations['cprf_percent'], color='red', s=0.05, label="CPRF " + cprf_string)
lgnd = plt.legend(loc="upper left", scatterpoints=1, fontsize=10)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
plt.xlabel("turnout")
plt.ylabel("party result")
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()

#%% Ballot staffing. Stuff till 47%

from random import uniform
city_stations = city_stations.sample(frac=1)
city_stations['fraud'] = False

i = 0
ur_percent = city_stations['ur'].sum()/city_stations['voted'].sum()
for index, row in city_stations.iterrows():
    if ur_percent < 0.47:
        total_voters = row['total_voters']
        voted = row['voted']
        max_fraud = total_voters - voted
        min_fraud = max_fraud*0.05
        number = int(uniform(min_fraud, max_fraud))
        city_stations.loc[index, 'ur'] = row['ur'] + number
        city_stations.loc[index, 'voted'] = row['voted'] + number
        city_stations.loc[index,'fraud'] = True
        ur_percent = city_stations['ur'].sum()/city_stations['voted'].sum()

city_stations['turnout'] = city_stations['voted']/city_stations['total_voters']
city_stations['ur_percent'] = city_stations['ur']/city_stations['voted']
city_stations['cprf_percent'] = city_stations['cprf']/city_stations['voted']

er_string = str(round(100*city_stations['ur'].sum()/city_stations['voted'].sum(),2)) + '%'
cprf_string = str(round(100*city_stations['cprf'].sum()/city_stations['voted'].sum(),2))+ '%'
plt.scatter(city_stations['turnout'], city_stations['ur_percent'], color='blue', s=0.05, label="United Russia " + er_string)
plt.scatter(city_stations['turnout'], city_stations['cprf_percent'], color='red', s=0.05, label="CPRF " + cprf_string)
lgnd = plt.legend(loc="upper left", scatterpoints=1, fontsize=10)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
plt.xlabel("turnout")
plt.ylabel("party result")
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()

#%% Misrecording of votes till 49.8

city_stations_change = city_stations[~city_stations['fraud']]
for index, row in city_stations_change.iterrows():
    if ur_percent < 0.4982:
        total_voters = row['total_voters']
        random_voted = int(uniform(total_voters * 0.8, total_voters))
        voted = random_voted
        random_er = int(uniform(random_voted * 0.8, random_voted))
        city_stations.loc[index, 'voted'] = voted
        city_stations.loc[index, 'ur'] = int(random_er)
        city_stations.loc[index, 'cprf'] = int((random_voted - random_er)*0.3)
        city_stations.loc[index, 'fraud'] = True
        ur_percent = city_stations['ur'].sum() / city_stations['voted'].sum()

city_stations['turnout'] = city_stations['voted']/city_stations['total_voters']
city_stations['ur_percent'] = city_stations['ur']/city_stations['voted']
city_stations['cprf_percent'] = city_stations['cprf']/city_stations['voted']

er_string = str(round(100*city_stations['ur'].sum()/city_stations['voted'].sum(),2)) + '%'
cprf_string = str(round(100*city_stations['cprf'].sum()/city_stations['voted'].sum(),2))+ '%'
plt.scatter(city_stations['turnout'], city_stations['ur_percent'], color='blue', s=0.05, label="United Russia " + er_string)
plt.scatter(city_stations['turnout'], city_stations['cprf_percent'], color='red', s=0.05, label="CPRF " + cprf_string)
lgnd = plt.legend(loc="upper left", scatterpoints=1, fontsize=10)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
plt.xlabel("turnout")
plt.ylabel("party result")
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()

#%% Core plot

city_stations_ok = city_stations[city_stations['fraud'] == False]
er_string = str(round(100*city_stations_ok['ur'].sum()/city_stations_ok['voted'].sum(),2)) + '%'
cprf_string = str(round(100*city_stations_ok['cprf'].sum()/city_stations_ok['voted'].sum(),2))+ '%'
plt.scatter(city_stations_ok['turnout'], city_stations_ok['ur_percent'], color='blue', s=0.05, label="United Russia " + er_string)
plt.scatter(city_stations_ok['turnout'], city_stations_ok['cprf_percent'], color='red', s=0.05, label="CPRF " + cprf_string)
lgnd = plt.legend(loc="upper left", scatterpoints=1, fontsize=10)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
plt.xlabel("turnout")
plt.ylabel("party result")
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()

#%% Tails plot

city_stations_fraud = city_stations[city_stations['fraud'] == True]
er_string = str(round(100*city_stations_fraud['ur'].sum()/city_stations_fraud['voted'].sum(),2)) + '%'
cprf_string = str(round(100*city_stations_fraud['cprf'].sum()/city_stations_fraud['voted'].sum(),2))+ '%'
plt.scatter(city_stations_fraud['turnout'], city_stations_fraud['ur_percent'], color='blue', s=0.05, label="United Russia " + er_string)
plt.scatter(city_stations_fraud['turnout'], city_stations_fraud['cprf_percent'], color='red', s=0.05, label="CPRF " + cprf_string)
lgnd = plt.legend(loc="upper left", scatterpoints=1, fontsize=10)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
plt.xlabel("turnout")
plt.ylabel("party result")
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()

#%% Teach Logistic Regression model on city stations

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegressionCV
pipe = Pipeline([("scale", StandardScaler()), ("model", LogisticRegressionCV())])
pipe.get_params()
X = city_stations[['ur','cprf', 'voted','total_voters']]
y = city_stations['fraud']
pipe.fit(X, y)
pipe.get_params()

#%% Apply model to all stations

stations['turnout'] = stations['voted']/stations['total_voters']
stations['ur_percent'] = stations['ur']/stations['voted']
stations['cprf_percent'] = stations['cprf']/stations['voted']
Xx = stations[['ur','cprf', 'voted','total_voters']]
prediction = pipe.predict(Xx)
prediction
stations['prediction'] = prediction

#%% Tails plot

stations_fraud = stations[stations['prediction'] == True]
er_string = str(round(100*stations_fraud['ur'].sum()/stations_fraud['voted'].sum(),2)) + '%'
cprf_string = str(round(100*stations_fraud['cprf'].sum()/stations_fraud['voted'].sum(),2))+ '%'
plt.scatter(stations_fraud['turnout'], stations_fraud['ur_percent'], color='blue', s=0.05, label="United Russia " + er_string)
plt.scatter(stations_fraud['turnout'], stations_fraud['cprf_percent'], color='red', s=0.05, label="CPRF " + cprf_string)
lgnd = plt.legend(loc="upper left", scatterpoints=1, fontsize=10)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
plt.xlabel("turnout")
plt.ylabel("party result")
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()

#%% Core plot

stations_ok = stations[stations['prediction'] == False]
er_string = str(round(100*stations_ok['ur'].sum()/stations_ok['voted'].sum(),2)) + '%'
cprf_string = str(round(100*stations_ok['cprf'].sum()/stations_ok['voted'].sum(),2))+ '%'
plt.scatter(stations_ok['turnout'], stations_ok['ur_percent'], color='blue', s=0.05, label="United Russia " + er_string)
plt.scatter(stations_ok['turnout'], stations_ok['cprf_percent'], color='red', s=0.05, label="CPRF " + cprf_string)
lgnd = plt.legend(loc="upper left", scatterpoints=1, fontsize=10)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
plt.xlabel("turnout")
plt.ylabel("party result")
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()

#%% Calculate number of votes fraud

ur_true = stations_ok['ur'].sum()/stations_ok['voted'].sum()
ur_fraud = stations_fraud['ur'].sum()/stations_fraud['voted'].sum()
round(stations_fraud['voted'].sum()*ur_true/ur_fraud)

#%% Table with experiment results for regions

pd.set_option('display.max_rows', 100)
regions = stations['region'].drop_duplicates()
region_result = pd.DataFrame()
stations_map = pd.DataFrame()
i=0
for region in regions:
    i+=1
    region_data = stations[stations['region'] == region]
    region_core_data = stations_ok[stations_ok['region'] == region]
    region_ur_core_percent = round(100*region_core_data['ur'].sum()/region_core_data['voted'].sum(),2)
    region_cprf_core_percent = round(100*region_core_data['cprf'].sum()/region_core_data['voted'].sum(),2)
    region_fraud_data = stations_fraud[stations_fraud['region'] == region]
    region_ur_percent_fraud = round(100*region_fraud_data['ur'].sum()/region_fraud_data['voted'].sum(),2)
    region_ur_percent = round(100*region_data['ur'].sum()/region_data['voted'].sum(),2)
    region_total_voted = region_data['total_voters'].sum()
    availability = round(100*region_core_data['total_voters'].sum()/region_total_voted,2)
    region_data['availability'] = availability
    stations_map = stations_map.append(region_data)
    total = len(region_data)
    fraud = len(region_fraud_data)
    ok = len(region_core_data)
    region_result = region_result.append(pd.DataFrame({'region name':region,'UR percent': region_ur_percent, 'UR core percent' : region_ur_core_percent , 'CPRF core percent' : region_cprf_core_percent , 'Stations with fraud' : fraud, 'Stations without fraud' : ok, 'Availability' : availability}, index=[i]))
region_result.sort_values('Availability')

#%% Map with availibility for citizens for voting

import plotly.express as px
fig = px.scatter_mapbox(stations_map, #our data set
                        lat="lat",
                        lon="lon",
                        color="availability",
                        range_color = (0,100),
                        zoom=2,
                        width=1200, height=800,
                        center = {'lat':60,'lon':105},
                        title =  'Availability - percentage of population in a region that has access to  voting stations with proper election results registration')
fig.update_layout(mapbox_style="open-street-map")
fig.update_traces(marker=dict(size=3))
fig.show(config={'scrollZoom': True})
