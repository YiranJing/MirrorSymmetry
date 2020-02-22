# Detecting Mirror Symmetry

## About

Bilateral Symmetry is renamed as mirror symmetry. In this project, I will write a computer program to detect mirror symmetry objects within the given image, and add mirrors line according to the algorithm in paper [Detecting Symmetry and Symmetric Constellations of Features] (http://www.cse.psu.edu/~yul11/CourseFall2006_files/loy_eccv2006.pdf) by Loy and Eklundh.

At a high level, the program compares the feature points on the image to those on the reflected version of the image, and then draws mirror lines based on the dominating symmetry pairs.

## Usage

You need OpenCV, Matplotlib, and NumPy to run the script

```sh
python detect.py example # show an example with details
```
```sh
python detect.py test  # show other test cases
```


## Detecting Steps:

**The approach is based on the simple idea of matching symmetric pairs of feature points**.


1. Translate input image and its reflective version into numerical array/matrix (i.e. a collection of points with row and column index)
2. Extract and Normalise features:
   - Find the key points (some sort of distinctive point) and descriptors with SIFT (a feature detection algorithm)
   - Normalise orientation: Convert angles from degrees to radians (pi*radians = 180 degrees)
3. Matching pairs of features: # 下面一段话再从新总结
Using KNN algorithm to match pairs of symmetry key points between original image and its reflective version.

Generates a collection of matched pairs of feature points. Each feature can be represented by a point vector describing its location in x, y co-ordinates, and its orientation φ. Symmetry can then be computed directly from these pairs of point vectors.

4. Draw mirror lines based on the dominant symmetry pairs

rij =xccosθij +ycsinθij

和图片2 对应angle_with_x_axis 公式解释

The 'votes'


# A Hexbin plot is useful to represent the relationship of 2 numerical variables when you have a lot of data point.
# Instead of overlapping, the plotting window is split in several hexbins, and the number of points per hexbin is counted.
# The color denotes this number of points.
这里给一个蝴蝶的带有hexplot的example

Each pair of matching points defines a potential axis of symmetry passing perpendicularly through the mid-point of the line joining pi and pj , shown by the dash-dotted line in





How does the symmetry detection work? At a high level, essentially what
is does is compare feature points on the image to those on the
reflected version of the image. A feature point is essentially some sort
of distinctive point (really a small region around a point), like an edge,
corner, or something. These are found using the Scale Invariant Feature Transform (SIFT).

With each feature point comes its descriptor, which characterizes the region
right around that point. What this means is, if you were to have two different photographs of the same object and ran SIFT on each picture, ideally a keypoint at a certain spot on the object in image 1 should have a descriptor very similar to the descriptor on a point on the object in image 2 that corresponds to the same 'part' of the object.

In this case, our two images are the original and a flipped/mirrored version of it. Then, keypoints of original are matched with those of mirrored version based on how similar the descriptor is. The idea is that the mirrored keypoint is the reflected version from the original, that now looks like the original after reflection. Then, a weighted vote is cast for the line of symmetry that would create such a reflection.

The 'votes' are tallied and the result is the hexbin plot of (r, theta) values, which represent a line in polar coordinates.

## Performance

缺点是不管图片对不对称，它都能画出来线
