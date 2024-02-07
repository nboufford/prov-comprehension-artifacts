library(stats)
library(utils)

df <- read.csv("data.csv")

write.csv(df[0:1], "temp_data.csv")

