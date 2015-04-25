import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#map = Basemap(projection='merc', resolution='h', fix_aspect=True, llcrnrlon=119.0, llcrnrlat=21.8, urcrnrlon=122.05 , urcrnrlat=25.4, lat_ts =20)
map = Basemap(projection='merc', area_thresh=0.1, resolution='h', llcrnrlon=119.0, llcrnrlat=21.8, urcrnrlon=122.05 , urcrnrlat=25.4)
map.drawcoastlines(linewidth=1)
#map.fillcontinents(color='coral')

lon = 121.6333
lat = 25.0333
taipei_x, taipei_y = map(lon, lat)
map.plot(taipei_x, taipei_y, 'bo')

plt.show()
