#step 1 import libraries and modules
import numpy as np
np.random.seed(123)  # for reproducibility

from keras.models import Sequential
# imported a sequential model type that is a linear stack of neural network layers.
from keras.layers import Dense, Dropout, Activation, Flatten
#these cores layers are used in almost any neural network
from keras.layers import Convolution2D, MaxPooling2D
# these are CNN layers that will help to train on image data
from keras.utils import np_utils
#step 2 load image data from MNIST
#importing utilities will help to transform the data
from keras.datasets import mnist

# Load pre-shuffled MNIST data into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print X_train.shape
# (60000, 28, 28)
from matplotlib import pyplot as plt
plt.imshow(X_train[0])
#it is important to visualize the data before
#step 3 preprocess input data for Keras
X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
#we want to transform our dataset from having shape(n, width, height) to (n, depth,width,height )

#we are going to print X_train's dimension again
print X_train.shape
# (60000, 1, 28, 28)
# we will need to convert our data type to float32 and normalize our data values to the range[0,1]
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Step 4 Preprocess class labels for Keras


