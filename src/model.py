import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(1250, activation='relu', return_sequences=True, input_shape=input_shape))
    # Add more layers as needed; for example, another LSTM or Dense layers.
    model.add(LSTM(1250, activation='relu'))
    model.add(Dense(1))  # predicting next month return
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse')
    return model
