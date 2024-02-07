SUCCEED = True

import pandas as pd

df = pd.read_csv("temp_data.csv")

if SUCCEED:
    with open("model.ckpt", "w+") as model:
        model.write("hello world!")