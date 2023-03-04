# Produce by Joshua

# University of Aberdeen

# Development time: 2023/3/2 1:53

import pandas as pd

data = pd.read_csv("rating.csv")
res = data.dropna(how="all")
res.to_csv("graders.csv", index=False)