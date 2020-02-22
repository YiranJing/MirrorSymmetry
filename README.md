# Detecting Mirror Symmetry

## Introduction

Bilateral Symmetry is renamed as mirror symmetry. In this project, I will write a computer program to detect mirror symmetry objects within the given image, and add mirrors line according to the algorithm in paper [Detecting Symmetry and Symmetric Constellations of Features](http://www.cse.psu.edu/~yul11/CourseFall2006_files/loy_eccv2006.pdf) by Loy and Eklundh.

At a high level, the program compares the feature points on the image to those on the reflected version of the image, and then draws mirror lines based on the dominating symmetry pairs.

## Usage

You need `OpenCV`, `Matplotlib`, and `NumPy` to run the script

```sh
python detect.py example # show an example with details
```
```sh
python detect.py test  # show other test cases
```


## Detecting Steps:

**The approach is based on the simple idea of matching symmetric pairs of feature points**.

The approach is based on the simple idea of matching symmetric pairs of feature points.  You can find the following steps in `detecting_mirrorLine`  function in `mirror_symmetry.py`.

1. Translate image and its reflective version into numerical array/matrix (i.e. a collection of points with row and column index)

2. Extract key features:
   - Find the key points (some sort of distinctive point) and descriptors with SIFT (a feature detection algorithm provided in OpenCV library). Each feature can be represented by a point vector describing its location in x, y coordinates, and its orientation.

3. Matching pairs of features:
   - Using `BFMatcher` (feature matching method provided in OpenCV) to match pairs of symmetry key points between original image and its reflective version. Then generates a collection of matched pairs of feature points called `matchpoints`, which is sorted by the distance between each pair of descriptors. The lower the distance, the better the symmetry match.
   - Normalise orientation of mirror feature: Convert angles from degrees to radians (𝝅*radians = 180 degrees) within [0,2𝝅].
   - Symmetry of each pair of points then is computed directly with (r, θ) values (polar coordinates).
![](https://github.com/YiranJing/MirrorSymmetry/blob/master/output/algo.png)

4. Finally Draw mirror lines based on the highest 'votes' from the result of the hexbin plot (the highest count of (r, θ)), which represents a line in polar coordinates.

## Performance
#### Butterfly Example
![](https://github.com/YiranJing/MirrorSymmetry/blob/master/output/example.png)
The left figure shows the top 10 pairs of mirror symmetry points. The yellow point of the middle plot is (6.18
, 2,42) (the (r, θ) values with the highest votes), which is the mirror line in polar coordinates (see right figure).

### Test case
#### Animals, human and architecture
![](https://github.com/YiranJing/MirrorSymmetry/blob/master/output/test1.png)

The testing results of symmetry animal and human face, and symmetry architecture looks good.

#### Symmetry object with shadow, reflection and rotational Symmetry
![](https://github.com/YiranJing/MirrorSymmetry/blob/master/output/test2.png)

My current algorithm cannot draw mirror line correctly for the symmetry object with shadow (left image). And it cannot identify the reflection of object. See the middle image, the correct mirror line should be horizontal between the mountain and its reflection. Also, it draws a random line on the rotational symmetry object (right image).

#### Multiple symmetry object within one image
![](https://github.com/YiranJing/MirrorSymmetry/blob/master/output/test3.png)

If the input image contains more than one symmetry object, my code can identify one of mirror symmetry object (left image), or fail to identify any one of them(right image).

See more test cases in [Detect_SymmetryPattern.ipynb](https://github.com/YiranJing/MirrorSymmetry/blob/master/Detect_SymmetryPattern.ipynb).
