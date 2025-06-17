import preswald

from preswald import connect, get_df
from preswald import query
from preswald import table, text
from preswald import plotly
import plotly.express as px
import pandas as pd

connect()  # Initialize connection to preswald.toml data sources
df = get_df("data/personality_dataset.csv")  # Load data

df['Friends_circle_size'] = pd.to_numeric(df['Friends_circle_size'], errors='coerce')
df['Going_outside'] = pd.to_numeric(df['Going_outside'], errors='coerce')

sql = "SELECT * FROM 'data/personality_dataset.csv' WHERE personality = 'Introvert'"
filtered_df = query(sql, "data/personality_dataset.csv")

text("# Introvert Personality Data")
table(filtered_df, title="Filtered Data")

fig = px.scatter(df, x='Going_outside', y='Friends_circle_size', color='Personality')
plotly(fig)