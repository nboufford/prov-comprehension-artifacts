import pandas as pd

with open("model.ckpt", 'r') as input_model:
    contents = input_model.read()

print("Evaluating...")

print("This isn't a model, this is just some random file with a ckpt file extension!")