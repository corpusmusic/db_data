import numpy as np
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from mpl_toolkits.basemap import Basemap


locations = np.genfromtxt("geo_information_nan.csv", 
                           delimiter=',', 
                           skip_header=1, 
                           dtype=str,
                           usecols=(0,1))

cnt = 0
geolocator = Nominatim()
geoinfo = np.array(['track_id', 'artist_location', 'location_latitude', 'location_longitude'])
for loc_array in locations:
  loc_array[1] = str(loc_array[1]).replace('/',' ')
  loc_array[1] = loc_array[1].replace("&amp;", " ")
  try:
    loc = geolocator.geocode(loc_array[1], timeout=5)
    if loc is None:      
      print "can not find the coordinates of %s"%(loc_array[1])
      continue
    loc_array = np.hstack((loc_array, loc.latitude))
    loc_array = np.hstack((loc_array, loc.longitude))    
    #print loc_array
  except GeocoderTimedOut as e:
    print("Error: geocode failed on input %s with message %s"%(loc_array[1], e.msg))
  geoinfo = np.vstack((geoinfo, loc_array))
  cnt += 1

with open('geo_information_nan_location_coordinates.csv', 'w') as f:
  np.savetxt(f, geoinfo, delimiter=',', fmt="%s")

print "conversion total: %d, success: %d, failure: %d"%(locations.size, cnt, locations.size-cnt)