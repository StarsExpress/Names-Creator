from configs.models_config import PAD_VALUE, NEURONS_UNITS, ACTIVATIONS, DROPOUT_RATE, LOSS_FUNCTION, LEARNING_RATE
from keras import metrics, Sequential, optimizers
from keras.layers import Masking, LSTM, Dense


def make_stacked_lstm(
        input_shape: tuple[int, int],  # (timesteps, features).
        lstm_metrics: list[metrics],
):
    model = Sequential()

    # 1st masking layer: specify input shape.
    model.add(Masking(mask_value=PAD_VALUE, input_shape=input_shape))
    # 1st LSTM layer: specify input shape & return sequences.
    model.add(
        LSTM(
            NEURONS_UNITS[0],
            activation=ACTIVATIONS[0],
            input_shape=input_shape,
            return_sequences=True,
            dropout=DROPOUT_RATE,
            recurrent_dropout=DROPOUT_RATE,
        )
    )

    model.add(Masking(mask_value=PAD_VALUE))  # 2nd masking layer.
    model.add(  # 2nd LSTM layer.
        LSTM(
            NEURONS_UNITS[1],
            activation=ACTIVATIONS[1],
            dropout=DROPOUT_RATE,
            recurrent_dropout=DROPOUT_RATE,
        )
    )

    # Output layer: shape of features count.
    model.add(Dense(input_shape[-1], activation=ACTIVATIONS[-1]))
    model.compile(
        loss=LOSS_FUNCTION,
        optimizer=optimizers.Adafactor(learning_rate=LEARNING_RATE),
        metrics=lstm_metrics,
    )

    return model
