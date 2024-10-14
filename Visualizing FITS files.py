# Visualizing FITS files

import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
plt.style.use(astropy_mpl_style) # styling output

with fits.open("jw05594-o086_t187_nircam_clear-f150w2_i2d.fits") as hdul: # opens the FITS file
    hdul.info()
    print(hdul[1].header)

image_file = get_pkg_data_filename("jw05594-o086_t187_nircam_clear-f150w2_i2d.fits") # extracts imagery data
image_data = fits.getdata(image_file, ext=1)


print(image_data.shape)

plt.figure() # initializes matplotlib figure
plt.imshow(image_data)
plt.colorbar()
plt.show()