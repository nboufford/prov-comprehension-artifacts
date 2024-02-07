import pandas as pd

filenames = ["model_1.ckpt", "model_2.ckpt", "model_3.ckpt"]

for filename in filenames:
    with open(filename, 'r') as input_model:
        contents = input_model.read()

print("Evaluating...")

print("The best model...was the model in our hearts all along!")