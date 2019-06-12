# Quickly generate trainset and validset from dataset
from sklearn.model_selection import train_test_split
[input: X and Y]
XTraining, XValidation, YTraining, YValidation = train_test_split(X,Y,stratify=Y,test_size=0.1) # before model building
[The model is built here...]
model.fit(XTraining,YTraining,batch_size=batchSize,epochs=amountOfEpochs,validation_data=(XValidation,YValidation),callbacks=callbackList)

# If the dataset is not standard dataset for classification, the method above may throw exceptions. 
# We can use another one, shuffle and split.

from numpy.random import shuffle
a = ['Spears', "Adele", "NDubz", "Nicole", "Cristina"]
b = [1,2,3,4,5]
z = zip(a, b)
# => [('Spears', 1), ('Adele', 2), ('NDubz', 3), ('Nicole', 4), ('Cristina', 5)]
shuffle(z)
a, b = zip(*z)
