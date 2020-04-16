import pandas as pd

df_scorecard = pd.read_csv('https://query.data.world/s/zxrfcjsdszuwmcm2y7svsm4ttcgfcf', encoding="iso-8859-1")
df_scorecard.to_csv("scorecard.csv")


df_completion = pd.read_csv('https://query.data.world/s/hqu3fnobwppzcjmjxldhlg3bdjyrrh', encoding="iso-8859-1")
df_completion.to_csv("completion.csv")