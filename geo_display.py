import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

marks_coordinates = np.genfromtxt("geo_information_coordinates.csv",
                                  delimiter=',', 
                                  dtype=[('lat', np.float32), ('lon', np.float32)], 
                                  usecols=(2, 3))

marks_nan = np.genfromtxt("geo_information_nan_location_coordinates.tsv",
                          delimiter='\t', 
                          dtype=[('lat', np.float32), ('lon', np.float32)], 
                          usecols=(2, 3))

fig = plt.figure()

#for U.S -130, 20, -60, 50
#for world -180, -60, 180, 90
themap = Basemap(projection='gall',
                 llcrnrlon = -180,              # lower-left corner longitude
                 llcrnrlat = -60,               # lower-left corner latitude
                 urcrnrlon = 180,               # upper-right corner longitude
                 urcrnrlat = 90,               # upper-right corner latitude
                 resolution = 'c',
                 area_thresh = 100000.0,)

themap.drawcoastlines()
themap.drawcountries()
themap.fillcontinents(color = 'gainsboro')
themap.drawmapboundary(fill_color='steelblue')

x1, y1 = themap(marks_coordinates['lon'], marks_coordinates['lat'])
themap.plot(x1, y1, 
            'x',                    # marker shape
            #color='Indigo',         # marker colour
            color='r',         # marker colour
            markersize=4            # marker size
            )

x2, y2 = themap(marks_nan['lon'], marks_nan['lat'])
themap.plot(x2, y2, 
            'o',                    # marker shape
            #color='Indigo',         # marker colour
            color='c',         # marker colour
            markersize=4            # marker size
            )

plt.show()