import numpy as np
np.random.seed(123)  # for reproducibility

from keras.models import Sequential
# imported a sequential model type that is a linear stack of neural network layers.
from keras.layers import Dense, Dropout, Activation, Flatten
#these cores layers are used in almost any neural network
from keras.layers import Convolution2D, MaxPooling2D
# these are CNN layers that will help to train on image data
from keras.utils import np_utils
#importing utilities will help to transform the data
from keras.datasets import mnist

# Load pre-shuffled MNIST data into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print X_train.shape
# (60000, 28, 28)
from matplotlib import pyplot as plt
plt.imshow(X_train[0])


