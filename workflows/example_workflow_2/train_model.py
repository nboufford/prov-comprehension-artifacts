import pandas as pd
import sys

arg = sys.argv[1:]

print(arg)


df = pd.read_csv("data.csv")

if arg[1] == '0.1':
    filename = "model_1.ckpt"
elif arg[1] == '0.01':
    filename = "model_2.ckpt"
else: 
    filename = "model_3.ckpt"


with open(filename, "w+") as model:
    model.write("hello model")
    