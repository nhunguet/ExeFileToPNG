

import numpy as np
from PIL import Image
import os
#from os import list

# Define width and height
w, h = 300, 300
cnt= 0;


# Read file using numpy "fromfile()"
for file in os.listdir('./testmode/'):
    if (file == '.DS_Store'):
        continue

    with open('./testmode/'+file, 'rb') as f:
        d = np.fromfile(f,dtype=np.uint8,count=w*h).reshape(h,w)
        # Make into PIL Image and save
        PILimage = Image.fromarray(d)
        PILimage.save('i'+str(cnt)+'.png')
    cnt += 1;