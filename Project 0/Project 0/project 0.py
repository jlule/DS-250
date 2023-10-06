#%%
import pandas as pd
import numpy as np
import altair as alt
#%%

link = "https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(link)


# %%
print(mpg
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"])
    .to_markdown(index=False))

# %%

chart = (alt.Chart(mpg)
  .encode(
    x='displ', 
    y='hwy')
  .mark_circle()
)

chart.save("altair_viz_1.png")


# %%
