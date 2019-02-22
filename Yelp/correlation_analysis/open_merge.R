library(foreign)
library(dplyr)

#path = "/Users/jinli/Projects/FAUI/Scenes_Data/Data/Merge20.background"
mydata = read.spss("/Users/jinli/Projects/FAUI/Scenes_Data/Data/MergeB-35.sav", to.data.frame=TRUE)
#write.table(head,"/Users/jinli/Projects/FAUI/Scenes_Data/Data/MergeB-35.csv")

head <- head(mydata)

glimpse(mydata)

col_names <- colnames(mydata)
write.csv(col_names)
