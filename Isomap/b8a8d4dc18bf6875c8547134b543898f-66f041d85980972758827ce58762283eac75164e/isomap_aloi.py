"""
 The ALOI, Amsterdam Library of Object Images, hosts a huge collection of 1000 small objects that were photographed in such a controlled 
 environment, by systematically varying the viewing angle, illumination angle, and illumination color for each object separately. 
 It can be accessed here: http://aloi.science.uva.nl/
 It shows that the isomap embedding appears to follow an easily traversable, 3D spline 
"""
import pandas as pd

from scipy import misc
from sklearn import manifold

import matplotlib.pyplot as plt

import os

# Look pretty...
plt.style.use('ggplot')


#
# Start by creating a regular old, plain, "vanilla"
# python list. 
#
samples = []
colours = []

#
# for-loop that iterates over the images in the
# Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
directory = "Datasets/ALOI/32/"
for fname in os.listdir(directory):
  fullname = os.path.join(directory, fname)
  img = misc.imread(fullname)
  # samples.append(  (img[::2, ::2] / 255.0).reshape(-1)  )   RESAMPLE
  samples.append( (img).reshape(-1) )
  colours.append('b') # blue colour

#
# appends to your list the images
# in the /Datasets/ALOI/32_i directory. 
#
directory = "Datasets/ALOI/32i/"
for fname in os.listdir(directory):
  fullname = os.path.join(directory, fname)
  img = misc.imread(fullname)
  # samples.append(  (img[::2, ::2] / 255.0).reshape(-1)  ) RESAMPLE
  samples.append( (img).reshape(-1) )
  colours.append('r')  # red colour

#
# Convert the list to a dataframe
#
df = pd.DataFrame( samples )


#
# Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)

my_isomap = iso.transform(df)


#
# Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("ISO transformation 2D")

ax.scatter(my_isomap[:,0], my_isomap[:,1], marker='.', c=colours)

#
# Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title("ISO transformation 3D")

ax.scatter(my_isomap[:,0], my_isomap[:,1], my_isomap[:,2], marker='.', c=colours)

plt.show()

