import numpy as np
from scipy.interpolate import RegularGridInterpolator,interp2d
from pyhdf import SD
import h5py

###Read Fy3 file
filename = r"K:\ZJQX\zjqx_dc\Satellite\秸秆焚烧\风云3D火点监测\FY3D_MERSI_GBAL_L1_20221115_0530_0250M_MS(1).HDF"
Handle  = h5py.File(filename, "r+")
Lat = Handle["Geolocation/Latitude"].value
Lon = Handle["Geolocation/Longitude"].value
fit_points = [np.linspace(0, 8200,410), np.linspace(0, 8000,400)]
[ut,vt]= [np.linspace(0, 8200,8200), np.linspace(0, 8000,8000)]
print(Lon.shape)


interp_lat = interp2d(fit_points[0],fit_points[1], Lat[:,:],kind="linear")
interp_lon = interp2d(fit_points[0],fit_points[1], Lon[:,:],kind="linear")
Lat_new = interp_lat(ut,vt)[:,:-8]
Lon_new = interp_lon(ut,vt)[:,:-8]
print(Lon_new.shape)
del Handle["Geolocation/Latitude"],Handle["Geolocation/Longitude"]
Lon = Handle.create_dataset("Geolocation/Longitude", data=Lon_new)
Lat = Handle.create_dataset("Geolocation/Latitude", data=Lat_new)
Handle.close()

# Lon = Handle.select("Latitude")
# def F(u, v):
#     return u * np.cos(u * v) + v * np.sin(u * v)

# fit_points = [np.linspace(0, 3, 8), np.linspace(0, 3, 8)]
# print(*fit_points)
#
# values = F(*np.meshgrid(*fit_points, indexing='ij'))
#
# ut, vt = np.meshgrid(np.linspace(0, 3, 80), np.linspace(0, 3, 80), indexing='ij')
#
# true_values = F(ut, vt)
#
# test_points = np.array([ut.ravel(), vt.ravel()]).T
#
# interp = RegularGridInterpolator(fit_points, values)
#
# im = interp(test_points, method="linear").reshape(80, 80)