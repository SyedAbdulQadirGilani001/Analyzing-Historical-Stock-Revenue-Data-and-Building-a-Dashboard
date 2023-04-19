install.packages("ggplot2") # for plotting
install.packages("cluster") # for kmeans
library(ggplot2) # for plotting
library(cluster) # for kmeans
acme <- read.csv("Acme3.csv", header = TRUE) # read the data
# barplot  
ggplot(acme, aes(x = V1, y = V2)) + geom_bar(stat = "identity", fill = "blue") + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) + 
  labs(x = "Year", y = "Revenue", title = "Acme Revenue")