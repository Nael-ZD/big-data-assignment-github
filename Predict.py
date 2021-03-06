# -*- coding: utf-8 -*-
"""keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VXKlIjbVKtm6xRBKA1y-81dXo6m7vmPh
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from numpy import loadtxt
import keras
from keras import optimizers
from keras import backend as k
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.metrics import categorical_crossentropy
import matplotlib.pyplot as plt
# %matplotlib inline #for google colaboratory drawing

model = Sequential([
                    Dense(14, input_shape=(14,), activation='relu'),
                    Dense(7, activation='relu'),
                    Dense(2, activation='softmax')
])


model.compile(optimizer=optimizers.RMSprop(learning_rate=0.001, rho=0.9),loss='categorical_crossentropy',metrics=['accuracy'])

dataset = loadtxt('dataSetLast.data.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:1500,1:15]
y = dataset[:1500,15:16]
y_t = keras.utils.to_categorical(y,num_classes=2)
z = dataset[:1500,16:17]
z_t = keras.utils.to_categorical(z,num_classes=2)

#print(y_t)
hist = model.fit(X,y_t,validation_split=0.1, batch_size=10, epochs=1000, shuffle=True, verbose=2)
model.save('hist.h5')



hist1 = model.fit(X,z_t,validation_split=0.1, batch_size=10, epochs=1000, shuffle=True, verbose=2)
model.save('hist1.h5')

plt.style.use('fivethirtyeight')
plt.plot((hist.history["accuracy"]),label='y accuracy')
#plt.plot(hist.history["loss"],label='loss')
plt.xlabel('epochs')
plt.ylabel('acc %')

plt.plot((hist1.history["accuracy"]),label='z accuracy')
#plt.plot(hist.history["loss"],label='loss')
plt.xlabel('epochs')
plt.title('Accuracy Graph')
plt.legend()
plt.grid(True)
plt.show()
