library(foreign)
library(dplyr)

#path = "/Users/jinli/Projects/FAUI/Scenes_Data/Data/Merge20.background"
#mydata = read.spss("/Users/jinli/Projects/FAUI/Scenes_Data/Data/MergeB-35.sav", to.data.frame=TRUE)
#write.table(head,"/Users/jinli/Projects/FAUI/Scenes_Data/Data/MergeB-35.csv")

mydata = read.spss("/Users/jinli/Projects/FAUI/Yelp/Data/US_merge_hyesun_final.sav", to.data.frame=TRUE)

head <- head(mydata)
#head

# this will view the file in another tab
View(head)

# this will print out what is viewed to the console
glimpse(mydata)


# find the column names
col_names <- colnames(mydata)
View(col_names)

row_names <-row.names(mydata)
View(row_names)


#write.csv(col_names)

# find the attributes of the dataframe
# will mainly use this to look at column name descriptions
View(attributes(head))
