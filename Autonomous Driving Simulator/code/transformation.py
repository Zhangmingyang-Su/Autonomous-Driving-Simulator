import os
import numpy as np
from sklearn.utils import shuffle
import ntpath

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail



def remove(num_bins, bins, samples_per_bin, column_element):
    remove_list = []
    for j in range(num_bins):
      list_ = []
      for i in range(len(column_element])):
        if column_element[i] >= bins[j] and column_element[i] <= bins[j+1]:
          list_.append(i)
      list_ = shuffle(list_)
      list_ = list_[samples_per_bin:]
      remove_list.extend(list_)
    return remove_list


def load_img_steering(datadir, df):
  image_path = []
  steering = []
  for i in range(len(data)):
    indexed_data = data.iloc[i]
    center, left, right = indexed_data[0], indexed_data[1], indexed_data[2]
    image_path.append(os.path.join(datadir, center.strip()))
    steering.append(float(indexed_data[3]))
    # left image append
    image_path.append(os.path.join(datadir,left.strip()))
    steering.append(float(indexed_data[3])+0.15)
    # right image append
    image_path.append(os.path.join(datadir,right.strip()))
    steering.append(float(indexed_data[3])-0.15)
  image_paths = np.asarray(image_path)
  steerings = np.asarray(steering)
  return image_paths, steerings
