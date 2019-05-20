from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
# create new figure, axes instances.
#fig=plt.figure()
#ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
m = Basemap()
bj_lat = 39.9042
bj_lon = 116.4076
am_lat = 52.3680
am_lon = 4.9036

wd_lat = 38.9072
wd_lon = -77.0369
m.drawgreatcircle(bj_lon, bj_lat, wd_lon, wd_lat,\
                  del_s = 1000, linewidth =1, color = 'b')
m.drawgreatcircle(bj_lon, bj_lat, am_lon, am_lat,\
                  del_s = 1000, linewidth =1, color = 'r')

m.drawcoastlines()
m.fillcontinents()
# draw parallels
m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
# draw meridians
m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
#ax.set_title('Great Circle from New York to London')
plt.show()