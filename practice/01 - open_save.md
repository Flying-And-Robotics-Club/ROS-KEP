```python
#!/usr/bin/env python

import numpy as np
import cv2

image_name = "tree"

print "Reading an image from file..."
img = cv2.imread("images/" + image_name + ".jpg");

print "Creating a window to hold the image..."
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

print "Displaying the image..."
cv2.imshow("Image", img)

print "Waiting for any key-press to generate copy..."
cv2.waitKey(0)

print "copy the image to new location..."
cv2.imwrite("images/copy/" + image_name + "-copy.jpg", img)
```