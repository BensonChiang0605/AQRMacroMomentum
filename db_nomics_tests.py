import pandas as pd
# import altair as alt
# alt.renderers.enable('notebook')

from dbnomics import fetch_series, fetch_series_by_api_link
df1 = fetch_series('NBS/M_A0B01/A0B0101')
print(df1.head())