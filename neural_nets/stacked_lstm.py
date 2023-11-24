from configs.models_config import PAD_VALUE, UNITS_LIST, ACTIVATIONS_LIST, DROPOUT_RATE, LOSS_FUNCTION, LEARNING_RATE
from keras import Sequential, optimizers
from keras.layers import Masking, LSTM, Dense


def make_stacked_lstm(input_shape, metrics_list):  # Input shape is a tuple of (timesteps, features).
    model = Sequential()

    # 1st masking layer: specify input shape.
    model.add(Masking(mask_value=PAD_VALUE, input_shape=input_shape))
    # 1st LSTM layer: specify input shape and return sequences.
    model.add(LSTM(UNITS_LIST[0], activation=ACTIVATIONS_LIST[0], input_shape=input_shape, return_sequences=True,
                   dropout=DROPOUT_RATE, recurrent_dropout=DROPOUT_RATE))

    # 2nd masking layer.
    model.add(Masking(mask_value=PAD_VALUE))
    # 2nd LSTM layer.
    model.add(LSTM(UNITS_LIST[1], activation=ACTIVATIONS_LIST[1], dropout=DROPOUT_RATE, recurrent_dropout=DROPOUT_RATE))

    # Output layer: shape of features count.
    model.add(Dense(input_shape[-1], activation=ACTIVATIONS_LIST[-1]))
    # Compile by Adafactor optimizer.
    model.compile(loss=LOSS_FUNCTION, optimizer=optimizers.Adafactor(learning_rate=LEARNING_RATE), metrics=metrics_list)

    return model
