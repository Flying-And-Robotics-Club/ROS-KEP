## Some Facts

* numpy - stores an image as a 2D pixel array
* BGR encoding is used as default

<hr>

## Some Commands to Try

```bash
python

>>> impport cv2
>>> import numpy as np
>>> img = cv2.imread("images/black_white.jpg")

>>> img
# outputs a 2d array representation of the 3 channel image

>>> type(img)
# <type 'numpy.ndarray'>

>>> img.size
# number of pixels in img

>>> img.shape
# (rows, columns, channels)

>>> img.dtype
# dtype('uint8')

>>> img[:,:,0]
# channel slicing

>>> blue,green,red = cv2.split(color_image)
# another way to slice channels
```

<hr>

## Things to Lookup

* Image Encoding
   - Grayscale
   - RGB
   - HSV
* Converting images from one encoding to another