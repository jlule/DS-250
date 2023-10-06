# %%
#import libraries
import pandas as pd
import altair as alt

# run in the text box on the right
# import sys
# !{sys.executable} -m pip install tabulate
# !{sys.executable} -m pip install altair_saver


# %%
#import data 
url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url)
# How does your name at your birth year compare to its use historically?
james = names.query('name == "James"')
james
total_james = james.sum()
total_james
utah = total_james[["UT"]]
utah
alabama = total_james[["AL"]]
alabama
georgia = total_james[["GA"]]
georgia
idaho = total_james[["ID"]]
idaho
# %%
#create table of all entries
table = total_james.head(60)
print(table.to_markdown(tablefmt="grid"))
# %%
# How does your name at your birth year compare to its use historically?
james = names.query('name == "James"')[["name", "year","Total"]]
james
chart = (alt.Chart(james).mark_bar().properties(title="Popularity of James")).encode(
x=alt.X('year', axis = alt.Axis(format="d", title="Year")),
y=alt.Y('Total', axis= alt.Axis(title="Number of People Named")))
chart
chart.save("james.png")

# chart1 = alt.Chart(james).mark_line().encode(
#     x='year',
#     y='Total'
# )
# %%
# If you talked to someone named Brittany on the phone, what is your guess of their age?
brittany = names.query('name == "Brittany"')[["name", "year","Total"]]
brittany
chart = (alt.Chart(brittany).mark_bar().properties(title="Given Name of Brittany")).encode(
x=alt.X('year', axis = alt.Axis(format="d", title="Year")),
y=alt.Y('Total', axis= alt.Axis(title="Number of People Named Brittany Over Time")))
chart
chart.save("Brittany.png")

chart1 = alt.Chart(brittany).mark_line().encode(
    x='year',
    y='Total'
)

chart1.save("project1qn2.png")

# %%
# Mary, Martha, Peter, and Paul and James are all religious names
christiannames = names.query("name == 'Mary' or name == 'Martha' or name == 'Peter' or name == 'Paul'")
christiannames
chart2 = alt.Chart(christiannames).mark_line().encode(
        x=alt.X('year'),
        y=alt.Y('Total'),
        color = 'name'
)

chart2
chart2.save("religiousname.png")

# %%
#Think of a unique name from a famous movie. Plot that name and see how increases line u
clint = names.query("name == 'Clint'")
chart3 = alt.Chart(clint).mark_bar().properties(title = "Popularity of Clint before after Heartbreak Ridge").encode(x='year',
y='Total')
# The highlight will be set on the result of a conditional statement
color=alt.condition(
alt.datum.year == 1955, # If the year is 1810 this test returns True,
alt.value('red'), # which sets the bar orange.
alt.value('steelblue') # And if it's not true it sets the bar steelblue.
)
line_plot_1 = (
alt.Chart(pd.DataFrame
    ({'x': [1980]}))
.mark_rule()
.encode(x='x'))

chart3 + line_plot_1

# %%