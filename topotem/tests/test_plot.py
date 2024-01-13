import matplotlib.pyplot as plt
plt.style.use("grayscale")
from matplotlib.colors import from_levels_and_colors

from topotem.dummy_data import get_polarisation_dummy_dataset
from topotem.polarisation import plot_polarisation_vectors
from topotem.polarisation import get_angles_from_uv

atom_lattice = get_polarisation_dummy_dataset(image_noise=True)
sublatticeA = atom_lattice.sublattice_list[0]
sublatticeB = atom_lattice.sublattice_list[1]
image = sublatticeA.signal

sampling = 0.1  # example of 0.1 nm/pix
units = 'nm'
image.axes_manager[-1].scale = sampling
image.axes_manager[-2].scale = sampling
image.axes_manager[-1].units = units
image.axes_manager[-2].units = units

sublatticeA.construct_zone_axes()
za0, za1 = sublatticeA.zones_axis_average_distances[0:2]

s_p = sublatticeA.get_polarization_from_second_sublattice(
    za0, za1, sublatticeB, color='blue')

vector_list = s_p.metadata.vector_list
x, y = [i[0] for i in vector_list], [i[1] for i in vector_list]
u, v = [i[2] for i in vector_list], [i[3] for i in vector_list]
angles = get_angles_from_uv(u, v, degrees=True)
# print(angles)

# Vector magnitude plot with red arrows:

# plot_polarisation_vectors(x, y, u, v, image=image,
#                           unit_vector=False, save=None,
#                           plot_style='vector', color='r',
#                           overlay=False, title='Vector Arrows',
#                           monitor_dpi=50)

#Vector magnitude plot with colormap viridis:

plot_polarisation_vectors(x, y, u, v, image=image,
                          unit_vector=False, save=None,
                          plot_style='triangles', monitor_dpi=50,
                          overlay=True, 
                          cmap='bwr', 
                          vector_rep='angle',
                          magnitude_multiplier=35,
                          triangle_base_length=0.2,
                        #   degrees=True,
                          )
plt.show()

print('Test successful.')