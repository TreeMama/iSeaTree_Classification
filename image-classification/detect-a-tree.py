#############################
##### AUTHOR: MADHU VP ######
#############################
#training - 
    #tree - 195 images
    #non-tree - 140 images
#validation -
    #tree - 50 images
    #non-tree - 30 images
#test
    #tree - 151 images
    #test - 112 images


# In[94]:


from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf 
import numpy as np
import cv2
import os


# In[20]:


img = image.load_img("basedata/train/tree/0ML44BUESTUX.jpg")
plt.imshow(img)


# In[21]:


cv2.imread("basedata/train/tree/0ML44BUESTUX.jpg").shape


# In[77]:


train = ImageDataGenerator(rescale = 1/255)
validation = ImageDataGenerator(rescale=1/255)
test = ImageDataGenerator(rescale = 1/255)


# In[73]:


train_dataset = train.flow_from_directory('basedata/train/',
                                         target_size=(200,200),
                                         class_mode='binary')


# In[74]:


validation_dataset = validation.flow_from_directory('basedata/validation/',
                                         target_size=(200,200),
                                         class_mode='binary')


# In[48]:


train_dataset.class_indices


# In[70]:


model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape = (200,200,3)),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    tf.keras.layers.Conv2D(32,(3,3), activation = 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    tf.keras.layers.Conv2D(64,(3,3), activation = 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(512,activation='relu'),
                                    tf.keras.layers.Dense(1,activation='sigmoid')
                                   
                                   ])


# In[71]:


model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(learning_rate=0.001),
              metrics=['accuracy'])


# In[75]:


model_fit = model.fit(train_dataset,
                     epochs=27,
                     validation_data = validation_dataset)


# In[ ]:


for i in validation_dataset:
    print(i.shape)


# In[60]:


dir_path = 'basedata/validation/tree/'

for i in os.listdir(dir_path):
    img = image.load_img(dir_path+'//'+i)
    plt.imshow(img)


# In[101]:


img = image.load_img('basedata/test/mixed/606.jpg', target_size=(200,200))
plt.imshow(img)
x = image.img_to_array(img)
x = np.expand_dims(x,axis=0)
images = np.vstack([x])
val = model.predict(images)
if val == 0:
    print("Not a tree")
else:
    print("This is a tree")


# In[98]:


dir_path = 'basedata/test/not-tree'

for i in os.listdir(dir_path):
    img = image.load_img(dir_path+'//'+i, target_size=(200,200))
    plt.imshow(img)

    x = image.img_to_array(img)
    x = np.expand_dims(x,axis=0)
    images = np.vstack([x])
    val = model.predict(images)
    if val == 0:
        print("Not a tree")
    else:
        print("This is a tree")

