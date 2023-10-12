import pandas as pd

df = pd.read_csv("temp_data.csv")

with open("model.ckpt", "w+") as model:
    model.write("hello world!")