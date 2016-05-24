library(ggmap)
library(ggplot2)


d <- read.csv('geo_information_coordinates_cluster.csv')
d1 <- read.csv('geo_information_nan_location_coordinates_cluster.csv')
summary(d)
summary(d1)

#For World
mapdata <- borders("world", colour="gray50", fill="gray50") # create a layer of borders
map <- ggplot() + mapdata

#For USA
mapdata <- get_map("usa", zoom = 3, scale = 1)

#For Europe
mapdata <- get_map("europe", zoom = 3, scale = 1)

map <- ggmap(mapdata, extent = "normal", maprange = TRUE)
map + geom_point(aes(x=longitude, y=latitude, color=cluster), data=d) + geom_point(aes(x=longitude, y=latitude, color=cluster), data=d1)
