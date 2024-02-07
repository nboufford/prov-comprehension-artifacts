import pandas as pd
import matplotlib.pyplot as plt

# Clean
df = pd.read_csv("data.csv")

new_df = df.drop(['Pregnancies'], axis=1)

new_df.to_csv('data_cleaned.csv', index=False)


# Plot
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

df = pd.read_csv('diabetes_output.csv')

df.set_index('BloodPressure').plot()

plt.savefig("plot.png")

