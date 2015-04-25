import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

map = Basemap(projection='merc', resolution='h', fix_aspect=True, llcrnrlon=118.0, llcrnrlat=21.8, urcrnrlon=122.50 , urcrnrlat=25.4, lat_ts =20)
#map = Basemap(projection='merc', area_thresh=0.1, resolution='h', llcrnrlon=119.0, llcrnrlat=21.8, urcrnrlon=122.05 , urcrnrlat=25.4)
map.drawcoastlines(linewidth=1)
map.fillcontinents(color='gainsboro')

twCountyDF = pd.read_csv('../sourceData/twCountyGeo.csv')
twFiremanDF = pd.read_csv('../sourceData/twFireman.csv')

mergedDF = twCountyDF.merge(twFiremanDF, on='County CH', how='inner')
mergedDF['Firemen Ratio'] = mergedDF['Population'] / mergedDF['Fireman'] 
lats = list(mergedDF['Latitude'])
lons = list(mergedDF['Longitude'])
firemen = list(mergedDF['Firemen Ratio'])
counties = list(mergedDF['County EN'])

# uncomment these 2 lines if you want to plot all dots at the same time
#x, y = map(lons, lats)
#map.plot(x, y, 'bo', markersize=8)

for county, fireman, lon, lat in zip(counties, firemen, lons, lats):
	x, y = map(lon, lat)
	map.plot(x, y, 'bo', markersize=fireman/50, alpha=0.2)
	plt.text(x+10000, y-5000, county, alpha=0.5, fontsize='smaller'	)

plt.show()


'''
data source: 
	county population: wikipedia
	fireman population: data.gov.tw
'''