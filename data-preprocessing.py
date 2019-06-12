# Quickly generate trainset and validset from dataset
from sklearn.model_selection import train_test_split
[input: X and Y]
XTraining, XValidation, YTraining, YValidation = train_test_split(X,Y,stratify=Y,test_size=0.1) # before model building
[The model is built here...]
model.fit(XTraining,YTraining,batch_size=batchSize,epochs=amountOfEpochs,validation_data=(XValidation,YValidation),callbacks=callbackList)
