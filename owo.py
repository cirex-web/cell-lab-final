import cv2
import numpy as np
from skimage import measure, segmentation
from scipy import ndimage

import matplotlib.pyplot as plt
import os


def load_images(folder:str,file_names:list[str], use_color = False):
    
  filepaths = []
  for filename in file_names:
    # if filename.endswith(".png") or filename.endswith(".jpg"):
    filepaths.append(os.path.join(folder, filename))

  return [cv2.imread(img_path, cv2.IMREAD_COLOR if use_color else cv2.IMREAD_GRAYSCALE) for img_path in filepaths]
  
def plot_images(images, horiz=False, figsize=None):
  fig, axes = plt.subplots(len(images), 1, figsize=figsize) if not horiz else \
        plt.subplots(1, len(images), figsize=figsize)
  for ax, img in zip(axes, images):
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    ax.axis('off')
  plt.subplots_adjust(wspace=0, hspace=0)  # Remove gaps between subplots
  plt.show()

# file_names = ["5s.png","10s.png","20s.png","60s.png","control.png","disinfectant.png"]
file_names = ["control","30s","15min","30min","60min","disinfectant2","control2","30s2","15min2","30min2","60min2","disinfectant2"][:2]
file_names = [f+".JPG" for f in file_names]
colored_images = load_images("new_pics",file_names,use_color=True)
def crop_circle(image):
  height, width = image.shape[:2]
  center = (width // 2, height // 2)
  radius = min(center[0], center[1], width - center[0], height - center[1])
  mask = np.zeros((height, width), dtype=np.uint8)
  cv2.circle(mask, center, radius, 255, -1)
  result = cv2.bitwise_and(image, image, mask=mask)
  return result
# print(colored_images)
# colored_images = [crop_circle(img) for img in colored_images]
plot_images(colored_images, horiz=True, figsize=(10, 10))

