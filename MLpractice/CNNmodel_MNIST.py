import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from keras.models import Sequential
from keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

np.random.seed(7)

train = pd.read_csv('/Users/45622/DevResources/MNIST_digits/train.csv')
test = pd.read_csv('/Users/45622/DevResources/MNIST_digits/test.csv')
X_train = (train.iloc[:, 1:].values).astype('float32')
y_train = (train.iloc[:, 0].values).astype('float32')
X_test = test.iloc[:, :].values.astype('float32')

X_train = X_train.reshape(X_train.shape[0], 28, 28)
X_test = X_test.reshape(X_test.shape[0], 28, 28)

X_train = X_train / 255.0
X_test = X_test / 255.0

y_train = to_categorical(y_train)

# for i in range(0, 9):
#     plt.subplot(331 + i)
#     plt.imshow(X_train[i], cmap=plt.get_cmap('gray'))

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

def cnn_model():
    model = Sequential()
    model.add(Conv2D(64, (5, 5), input_shape=(28, 28, 1), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(units=128, activation='relu'))
    model.add(Dense(units=50, activation='relu'))
    model.add(Dense(units=10, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=3, batch_size=128, verbose = 1)
    return model

model = cnn_model()

predictions = model.predict_classes(X_test, verbose=0)

submissions=pd.DataFrame({"ImageId": list(range(1,len(predictions)+1)),
                         "Label": predictions})
submissions.to_csv("DigitRecognitions3.csv", index=False, header=True)






