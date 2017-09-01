# Cheat Sheet
![konami](./images/konami2.png)

## Using Jupyter Notebooks
- shift+enter: run cell
- a: insert cell above
- b: insert cell below
- dd: delete cell
- Use an exclamation mark in the command to use linux commands. eg. `!mkdir data` will make a data directory.

## Typical keras model
Before you jump in to copying and pasting the model below answer these questions:
1.  Is it a regression/binary classifiction/ multi class classification problem? [see activation](#final-activation-function) and [loss function](#loss-function)
2. Is the X data real (floating point) numbers? Then normalise it so that
\begin{align}
X_{new} = \frac{X - mean(X)}{stddev(X)}
\end{align}.
Same with `y`.
3. Is the X data categorical? (eg. words, colours, car type). Then create a dictionary that will map categories to numbers. Then use the `Embedding` layer to input the data.

```
from keras.layers import Dense, Activation

# Must provide either input_dim or input_shape for the **first layer only**
model.add(Dense(units=64, input_dim=100, activation='relu'))
model.add(Dense(units=10))
model.add(Activation('softmax'))

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
```
Whatever the layer that you need, you simply add it (eg. `model.add(LSTM(...))`, `model.add(Dropout(...))`).

Training the model:
```
model.fit(X_train, y_train, epochs=5, batch_size=256)
```
Predicting with model:
```
model.predict(X_train, batch_size=256)
```

## Final Activation function
1. Regression - None or 'linear' (no activation implies linear)
2. Classifiction (two classes) - 'sigmoid'
3. Classifiction (multiple classes) - 'softmax'

## Loss function
1. Regression - 'mean_squared_error'
2. Classifiction (two classes) - 'binary_crossentropy'
3. Classifiction (multiple classes) - 'sparse_categorical_crossentropy'
It is sparse since with the other option 'categorical_crossentropy' you need to provide a one hot encoded version of the classes.

### References:
1. https://keras.io/
