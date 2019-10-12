import tensorflow as tf 

while True:
    try:
        name = input("Which model would you like to load? (Press ENTER for first model in directory)\n")
        model = tf.keras.models.load_model(f'models/{name}.h5')
    except Exception:
        print("Sorry please enter a valid name.")
    else:
        break

model.summary()