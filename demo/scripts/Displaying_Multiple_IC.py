#!/usr/bin/env python

# # Example: Displaying Multiple IonChromatogram Objects
#
# Multiple `IonChromatogram` objects can be plotted on the same figure.
#
# To start, load a datafile and create an `IntensityMatrix` as before.

# In[1]:

# 3rd party
from domdf_python_tools.paths import PathPlus

cwd = PathPlus('.').resolve()
data_directory = PathPlus('.').resolve().parent.parent / "datafiles"
# Change this if the data files are stored in a different location

output_directory = cwd / "output"

# 3rd party
from pyms.GCMS.IO.JCAMP import JCAMP_reader
from pyms.IntensityMatrix import build_intensity_matrix_i

jcamp_file = data_directory / "gc01_0812_066.jdx"
data = JCAMP_reader(jcamp_file)
tic = data.tic
im = build_intensity_matrix_i(data)

# Extract the desired IonChromatograms from the `IntensityMatrix`.

# In[2]:

ic73 = im.get_ic_at_mass(73)
ic147 = im.get_ic_at_mass(147)

# Import matplotlib and the `plot_ic()` function, create a subplot, and plot the ICs on the chart:

# In[3]:

# 3rd party
import matplotlib.pyplot as plt
from pyms.Display import plot_ic

fig, ax = plt.subplots(1, 1, figsize=(8, 5))

# Plot the ICs
plot_ic(ax, tic, label="TIC")
plot_ic(ax, ic73, label="m/z 73")
plot_ic(ax, ic147, label="m/z 147")

# Set the title
ax.set_title("TIC and ICs for m/z = 73 & 147")

# Add the legend
plt.legend()

plt.show()
