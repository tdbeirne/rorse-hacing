import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout
from tensorflow.keras.models import Sequential

# Need to implement data
horse_runs = np.loadtxt(open("data/runs.csv", "rb"),  delimiter=",", skiprows=1)

quit()

(x_train, y_train), (x_test, y_test) = horse_runs.load_data()

EPOCHS = 10
BATCH_SIZE = 128

DENSE_LAYER_SIZE = 256
DROPOUT_RATE = 0.4

NAME = f"{DENSE_LAYER_SIZE}-dense-{DROPOUT_RATE}-drop-{int(time.time())}"
print(NAME)

model = Sequential()
model.add(Dense(DENSE_LAYER_SIZE/2, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(DROPOUT_RATE))

model.add(Dense(DENSE_LAYER_SIZE, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(DROPOUT_RATE))

model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(DROPOUT_RATE))

model.add(Dense(2, activation='softmax'))

tensorboard = TensorBoard(log_dir=f"tensorboard_logs\{NAME}")

opt = tf.keras.optimizers.adam(lr=1e-3, decay=1e-6)

model.compile(optimizer=opt,
            loss='binary_crossentropy',
            metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=BATCH_SIZE, verbose=2,
        epochs=EPOCHS, validation_data=(x_test, y_test))


model.evaluate(x_test, y_test)

input("Would you like to save the model? (Press ANY key too save.)")

model.save(f'models/{NAME}.h5')
