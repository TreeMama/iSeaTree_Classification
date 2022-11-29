###########################
##### AUTHOR: MADHU VP ####
###########################


import random
from os import listdir
from numpy import asarray
from numpy import save
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from tensorflow.keras import layers
import tensorflow.keras as keras
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
from matplotlib.image import imread


# define location of dataset
folder = 'both/'
photos, labels = list(), list()
# enumerate files in the directory
for file in listdir(folder):
	# determine class
	output = 0.0
	if file.startswith('bir'):
		output = 1.0
	# load image
	photo = load_img(folder + file, target_size=(200, 200))
	# convert to numpy array
	photo = img_to_array(photo)
	# store
	photos.append(photo)
	labels.append(output)
# convert to a numpy arrays
photos = asarray(photos)
labels = asarray(labels)
print(photos.shape, labels.shape)
# save the reshaped photos
save('bir_vs_red_photos.npy', photos)
save('bir_vs_red_labels.npy', labels)


# load and confirm the shape
from numpy import load
photos = load('bir_vs_red_photos.npy')
labels = load('bir_vs_red_labels.npy')
print(photos.shape, labels.shape)


#train 
 #bir - 75
 #red - 75

#test
 #bir - 25
 #red - 25



# define cnn model
def define_model():
	model = keras.Sequential()
	model.add(layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(200, 200, 3)))
	model.add(layers.MaxPooling2D((2, 2)))
	model.add(layers.Flatten())
	model.add(layers.Dense(128, activation='relu', kernel_initializer='he_uniform'))
	model.add(layers.Dense(1, activation='sigmoid'))
	# compile model
	opt = SGD(learning_rate=0.001, momentum=0.9)
	model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
	return model


# define model
model = define_model()

# create data generator
datagen = ImageDataGenerator(rescale=1.0/255.0)


# prepare iterators
train_it = datagen.flow_from_directory('dataset_birch_vs_redwood/train/',
	class_mode='binary', batch_size=64, target_size=(200, 200))
test_it = datagen.flow_from_directory('dataset_birch_vs_redwood/test/',
	class_mode='binary', batch_size=64, target_size=(200, 200))


# fit model
history = model.fit(train_it, steps_per_epoch=len(train_it), validation_data=test_it, validation_steps=len(test_it), epochs=20, verbose=0)


# evaluate model
_, acc = model.evaluate(test_it, steps=len(test_it), verbose=0)
print('> %.3f' % (acc * 100.0))

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(200, 200))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 200, 200, 3)
	# center pixel data
	img = img.astype('float32')
	img = img - [123.68, 116.779, 103.939]
	return img


img = load_image('both/20.jpg')
result = model.predict(img)
if int(result) == 0:
    print("It's a paper birch")
else:
    print("It's a coastal redwood")
