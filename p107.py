import pandas as pd
import plotly.express as px

df=pd.read_csv("math.csv")
mean=df.groupby(["s","level"],as_index=False)["attempt"].mean()




fig=px.scatter(
    mean,
    x="s",
    y="level",
    size="attempt",
    color="attempt"
   
)
fig.show()  
