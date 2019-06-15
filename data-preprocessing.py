# Quickly generate trainset and validset from dataset
from sklearn.model_selection import train_test_split
[input: X and Y]
XTraining, XValidation, YTraining, YValidation = train_test_split(X,Y,stratify=Y,test_size=0.1) # before model building
[The model is built here...]
model.fit(XTraining,YTraining,batch_size=batchSize,epochs=amountOfEpochs,validation_data=(XValidation,YValidation),callbacks=callbackList)

# If the dataset is not standard dataset for classification, the method above may throw exceptions. 
# We can use another one, shuffle and split.
from sklearn.utils import shuffle
def get_train_valid(X, Y, validation_split=0.2):
    if validation_split >= 1 or validation_split <= 0:
        raise Exception()
    X, Y = shuffle(X, Y)
    train_len = int(len(X)*(1-validation_split))
    train_X = X[:train_len]
    train_Y = Y[:train_len]
    valid_X = X[train_len:]
    valid_Y = Y[train_len:]
    return train_X, train_Y, valid_X, valid_Y
# omit the rest of codes

# Split sentences into tokens
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
my_sent = "Hi man, how have you been?"
tokens = word_tokenize(my_sent)
