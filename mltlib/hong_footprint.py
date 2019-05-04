import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
plt.figure(figsize=(16,8))
m = Basemap()
m.drawcoastlines()

m.drawcountries(linewidth=1.5)
#n = Basemap(llcrnrlon=73, llcrnrlat=18, urcrnrlon=135, urcrnrlat=53)
#n.drawcoastlines()
plt.show()