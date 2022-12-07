# iSeaTree_Classification
A directory of classification code for the iSeaTree project

image-classification folder

1. detect-a-tree.py
A python code built using CNN and tensorflow to detect the presence of a tree in an image.
The directory structure of training and testing images are as follows:

basedata -> train, test
train -> tree, nottree
test -> tree, nottree

2. redwood-vs-birch.py
A python code built using CNN, Tensorflow and keras to classify images based on barktypes.
The 2 barktypes classified here are coastal redwood and paper birch
The current accuracy rate is 67%, because only 100 images are used to train
The directory structure of training and testing images are as follows:
dataset_redwood_vs_birch -> train, test
train -> birch, redwood
test -> birch, redwood

other

1. count-features.py - counts all the trees based on color, shape, direction, needle traits (if conifer) leaftype, barktype (if broadleaf)
2. find-an-entry.py - A menu-driven program to return the plant ID and common name of an entry based on a user-defined feature (present in the json file).
