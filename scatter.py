import pandas as pd 
import ploty.express as px

df = pd.read_csv("Copydata.csv")
fig = px.scatter(df, x = "date", y = "cases", size = "Percentage", color = "Country", size_max = 60)
fig.show()
