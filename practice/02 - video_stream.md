```python
#!/usr/bin/env python

import numpy as np
import cv2

print "Reading video from camera..."
video = cv2.VideoCapture(0)
# video = cv2.VideoCapture("videos/video.mp4")

while(True): # an infinite loop
    _, frame = video.read() # fetches a frame as image

    # process the image frame as needed
    cv2.imshow("Frame", frame) # shows the frame in a window
    if cv2.waitKey(10) & 0xFF == ord('q'): break
    # 10 frames/sec

# programming ethics :)
video.release()
cv2.destroyAllWindows()
```