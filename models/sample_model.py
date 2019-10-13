import time
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout
from tensorflow.keras.models import Sequential

# Need to implement data
horse_runs = np.loadtxt(open("data/runs_augmented.csv", "r"),  delimiter=",", skiprows=1)

# WARNING: if you try to re-train a model on re-shuffled data IT WILL MEMORIZE IT!!
np.random.shuffle(horse_runs) 

# Remove IDs and Place/Win
x = np.delete(horse_runs,[0,1,2,3,4,11,12,25],1) # 1-4 are ids, 11&12 are labels, 25 is time to finish

# 11 is the place order label
# 12 is the win label
delete_indicies = [x for x in range(0,len(horse_runs[0])) if x != 12]
y = np.delete(horse_runs, delete_indicies ,1)

train_size = 70000
x_train = x[:train_size]
x_test = x[train_size:]

y_train = y[:train_size]
y_test = y[train_size:]

quit()


EPOCHS = 10
BATCH_SIZE = 512
DENSE_LAYER_SIZE = 2048
DROPOUT_RATE = 0.4

NAME = f"{DENSE_LAYER_SIZE}-dense-{DROPOUT_RATE}-drop-{int(time.time())}"
print(NAME)

model = Sequential()

model.add(Dense(DENSE_LAYER_SIZE/2, activation='relu', input_shape=(20,) )) #input layer shape
model.add(BatchNormalization())
model.add(Dropout(DROPOUT_RATE))

model.add(Dense(DENSE_LAYER_SIZE, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(DROPOUT_RATE))

model.add(Dense(DENSE_LAYER_SIZE/2, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(DROPOUT_RATE))

model.add(Dense(1, activation='softmax'))

#tensorboard = TensorBoard(log_dir=f"tensorboard_logs\{NAME}")
#opt = tf.keras.optimizers.adam(lr=1e-3, decay=1e-6)

model.compile(optimizer="adam",
            loss='binary_crossentropy',
            metrics=['accuracy'])

model.summary()

model.fit(x_train, y_train, batch_size=BATCH_SIZE, verbose=1,
        epochs=EPOCHS, validation_data=(x_test, y_test))

model.evaluate(x_test, y_test, verbose=2)

if input("Would you like to save the model? (Press ENTER key too save.)") != '':
        model.save(f'trained_models/{NAME}.h5')
