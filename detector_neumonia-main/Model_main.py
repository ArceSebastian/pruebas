import tensorflow as tf
#from tensorflow.keras import models

def model_fun():
    model_cnn = tf.keras.models.load_model('WilhemNet_86.h5')
    return model_cnn    