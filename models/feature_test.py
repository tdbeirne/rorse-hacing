import time
import tensorflow as tf
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout, Sequential

# Need to implement data
# horse_runs = datasets.horse_runs

(x_train, y_train), (x_test, y_test) = horse_runs.load_data()

# List of features to test
dense_layers = [150]
dropout_layers = [0.38, 0.4, 0.42, 0.44, 0.46, 0.48, 0.5]


for dense_layer in dense_layers:
    for dropout_layer in dropout_layers:
        NAME = "{}-dense-{}-drop-{}".format(dense_layer, dropout_layer, int(time.time()))
        print(NAME)

        model = Sequential()
        model.add(Dense(dense_layer, activation='relu'))
        model.add(BatchNormalization())
        model.add(Dense(dense_layer, activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(dropout_layer))
        
        model.add(Conv2D(filters=64, kernel_size=3, activation='relu'))
        model.add(BatchNormalization())
        model.add(Conv2D(filters=64, kernel_size=3, activation='relu'))
        model.add(BatchNormalization())
        model.add(Conv2D(filters=64, kernel_size=5, strides=2, padding='same', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(dropout_layer))

        model.add(Flatten())
        model.add(Dense(dense_layer, activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(dropout_layer))
        model.add(Dense(10, activation='softmax'))

        tensorboard = TensorBoard(log_dir=f"logs3\{NAME}")

        opt = tf.keras.optimizers.adam(lr-1e-3, decay=1e-6)

        model.compile(optimizer='adam',
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])

        model.fit(x_train, y_train, batch_size=512, verbose=2,
                epochs=50, validation_data=(x_test, y_test), callbacks=[tensorboard])

        # No need to evaluate models because of tensorboard
        # model.evaluate(x_test, y_test)

        model.save(f'fmodels/{NAME}.h5')
