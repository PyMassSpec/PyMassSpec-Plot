#!/usr/bin/env python

# # Example: Displaying a TIC
#
# First, setup the paths to the datafiles and the output directory, then import `JCAMP_reader`.

# In[1]:

# 3rd party
from domdf_python_tools.paths import PathPlus

cwd = PathPlus('.').resolve()
data_directory = PathPlus('.').resolve().parent.parent / "datafiles"
# Change this if the data files are stored in a different location

output_directory = cwd / "output"

# 3rd party
from pyms.GCMS.IO.JCAMP import JCAMP_reader

# Read the raw data files and extract the TIC.

# In[2]:

jcamp_file = data_directory / "gc01_0812_066.jdx"
data = JCAMP_reader(jcamp_file)
tic = data.tic

# Import matplotlib and the `plot_ic()` function, create a subplot, and plot the TIC:

# In[3]:

# 3rd party
import matplotlib.pyplot as plt

# this package
from pymassspec_plot import plot_ic

fig, ax = plt.subplots(1, 1, figsize=(8, 5))

# Plot the TIC
plot_ic(ax, tic, label="TIC")

# Set the title
ax.set_title("TIC for gc01_0812_066")

# Add the legend
plt.legend()

plt.show()

# In addition to the TIC, other arguments may be passed to `plot_ic()`. These can
# adjust the line colour or the text of the legend entry.
# See https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.lines.Line2D.html for a
# full list of the possible arguments.
#
# An `IonChromatogram` can be plotted in the same manner as the TIC in the example above.
