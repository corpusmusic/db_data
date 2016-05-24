library(ggmap)
library(ggplot2)


d <- read.csv('geo_information_final_cluster.csv')

summary(d)

#For World
mapdata <- borders("world", colour="gray50", fill="gray50") # create a layer of borders
map <- ggplot() + mapdata

#For USA
mapdata <- get_map("usa", zoom = 3, scale = 1)

#For Europe
mapdata <- get_map("europe", zoom = 3, scale = 1)

map <- ggmap(mapdata, extent = "normal", maprange = TRUE)
map + geom_point(aes(x=longitude, y=latitude, color=cluster), data=d)+scale_colour_gradient(low="green", high="red")
