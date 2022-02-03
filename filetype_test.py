# file used to try and attain a usable description of a network from a tensorflow .ckpt or .h5 file

import tensorflow as tf
import numpy as np
import os

opt = tf.keras.optimizers.Adam(learning_rate=0.005)
model = tf.keras.Sequential([
                            tf.keras.layers.Dense(20, activation='relu'),
                            tf.keras.layers.Dense(10, activation='relu'),
                            tf.keras.layers.Dense(5, activation='relu')
])

model.compile(optimizer=opt,
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

inguy = np.zeros(20)

model.predict(inguy)

model.save(os.getcwd() + r'/models/m0.h5')

print(len(model.weights))


print("donesies\n")