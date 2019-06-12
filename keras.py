# model = some sort of Model() or Sequential()

# A sheet of details of your model
model.summary()

# Use checkpoint to keep the model of least valid loss during training
from keras.callbacks import ModelCheckpoint
filename = 'model.h5'
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
history = model.fit(trainX, trainY, epochs=30, batch_size=64, validation_data=(validX, validY), callbacks=[checkpoint], verbose=2)

# plot the loss curve
import matplotlib.pyplot as plt
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'valid'], loc='upper left')
plt.savefig(f"./model/loss.png")
plt.clf()
