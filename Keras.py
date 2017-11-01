from keras.models import Sequential
from keras.layers import Dense, Activation

# Simple feed-forward architecture
model = Sequential()
model.add(Dense(output_dim=64, input_dim=100))
model.add(Activation("relu"))
model.add(Dense(output_dim=10))
model.add(Activation("softmax"))

# Optimize with SGD
model.compile(loss='categorical_crossentropy',
              optimizer='sgd', metrics=['accuracy'])

# Fit model in batches
model.fit(X_train, Y_train, nb_epoch=5, batch_size=32)

# Evaluate model
loss_and_metrics = model.evaluate(X_test, Y_test, batch_size=32)