#%%

import pandas as pd
import altair as alt
import numpy as np
import json
import altair as alt


#%%

url = "https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json"
flights = pd.read_json(url)

# turn -999 to np.nan
# turn strings  "n/a" into actual  np.nan then 

fixers = flights.replace(-999, np.nan)

fixers = fixers.replace("n/a", np.nan)


# fixed = fixers.minutes_delayed_carrier.fillna(fixers.minutes_delayed_carrier.mean())

fixers2 = fixers
# fixers2.minutes_delayed_carrier.fillna(fixers2.minutes_delayed_carrier.mean())
fixers2.minutes_delayed_carrier = fixers2.minutes_delayed_carrier.fillna(fixers2.minutes_delayed_carrier.mean())
fixers2.num_of_delays_late_aircraft = fixers2.num_of_delays_late_aircraft.fillna(fixers2.num_of_delays_late_aircraft.mean())

fixers2.month

fixers2.month = fixers2.month.fillna(method='bfill')

flights = fixers2




# %%

print('this is the data columns')
print(flights.columns)


#%%
print(flights.shape)

#%%
flights.describe()


#%%
flights.head()
#%%
# Which airport has the worst delays? 
# How did you choose to define “worst”? 
# As part of your answer include a table
#  that lists the total number of flights,
#  total number of delayed flights, proportion of
#  delayed flights, and average delay time in hours, 
# for each airport.
delay_security = flights.num_of_delays_security
print(delay_security)
#%%
delay_carrier = flights.num_of_delays_carrier
print(delay_carrier)
#%%
delay_craft = flights.num_of_delays_late_aircraft
print(delay_craft)

delay = flights.groupby(['airport_code',]).sum().reset_index()
delay['Total_Delays'] = delay.minutes_delayed_total.div(delay.num_of_delays_total)

print(delay.to_markdown())


#%%
# What is the worst month to fly if you want to avoid delays? 
# Include one chart to help support your answer, with the x-axis
#  ordered by month. You also need to explain and 
#  justify how you chose to handle the missing Month data.


# delays = flights.groupby(['month']).sum().reset_index()



delays = flights.groupby(['month']).sum().reset_index()
print(delays)

chart = alt.Chart(delays).mark_circle(size=600).encode(
    x='month',
    y='num_of_delays_total',
)


chart
chart.save("project2chart.png")

# JULY


#%%

source = flights 

chart = alt.Chart(delays).mark_circle(size=60).encode(
    x='month',
    y='num_of_delays_total',
)
chart 
# chart.save("altair_viz_1.png")

# %%
# According to the BTS website the Weather category only accounts
#  for severe weather delays. Other “mild” weather delays are 
#  included as part of the NAS category and the Late-Arriving 
#  Aircraft category. Calculate the total number of flights 
#  delayed by weather (either severe or mild) using these two
#   rules:

# 30% of all delayed flights in the Late-Arriving category are due
#  to weather.

# From April to August, 40% of delayed flights in the NAS category
#  are due to weather. The rest of the months, the proportion rises
#   to 65%.

delays = flights.groupby(['month']).sum().reset_index()

delayss = flights.assign( severe = lambda x: x.num_of_delays_weather, nodla_nona = lambda x: 
x.num_of_delays_late_aircraft.replace(-999, np.NaN), mild_late = lambda x: x.nodla_nona.fillna(x.nodla_nona.mean()), 
mild = lambda x: np.where( x.month.isin(['April', 'May', 'June', 'July', 'August']), 

x.num_of_delays_nas * 0.4,
x.num_of_delays_nas * 0.65 ), 

total_delays_weather = lambda x: (x.severe + x.mild_late * .3 + x.mild) .apply(np.ceil) .round(decimals=0),
percent_weather = lambda x: (x.total_delays_weather / x.num_of_delays_total).round(decimals=2)) .filter(['airport_code','month','severe','mild', 'mild_late', 'total_delays_weather', 'num_of_delays_total', 'percent_weather'])



print(delayss.to_markdown())


#%%

# Create a barplot showing the proportion of all flights that 
# are delayed by weather at each airport. What do you learn from
#  this graph (Careful to handle the missing Late Aircraft data
#   correctly)?

chart6 = alt.Chart(delayss).mark_bar().encode(
    x='airport_code',
    y='total_delays_weather'
)

chart6



#%%

# Fix all of the varied NA types in the data to be consistent
#  and save the file back out in the same format that was 
#  provided (this file shouldn’t have the missing values 
#  replaced with a value). Include one record example from
#   your exported JSON file that has a missing value 
#   (No imputation in this file).

fixers.head(1).to_json()

