from keras import layers
from keras import Input
from keras.models import Model
from sklearn.metrics import *

def GRU_Train(max_feature, classes):
    X_input = Input(shape=(None,), dtype='int32', name='posts')
    embedded_posts = layers.Embedding(max_feature, 64)(X_input)
    x = layers.GRU(128)(embedded_posts)
    y = layers.Dense(classes, activation='sigmoid')(x)

    model = Model(X_input, y, name='gru')
    return model


def GRU_Score(x_train, y_train, x_test, y_test):
    model = GRU_Train(x_train.shape[1],1)
    model.compile(optimizer='rmsprop',loss='binary_crossentropy')
    model.fit(x_train, y_train, epochs=15, batch_size=4,validation_data=(x_test, y_test), verbose=2,shuffle=False)
    y_pred2 = model.predict(x_test)

    return y_pred2
