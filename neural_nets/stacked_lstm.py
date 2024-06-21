from configs.models_config import PAD_VALUE, LSTM_NEURONS, ACTIVATIONS, DROPOUT_RATE, LOSS_FUNCTION, LEARNING_RATE
from keras import metrics, Sequential, optimizers
from keras.layers import Masking, LSTM, Dense


def make_stacked_lstm(input_shape: tuple[int, ...], lstm_metrics: list[metrics]):
    """
    Create a stacked LSTM model with 2 masking layers and 2 LSTM layers.
    Output layer has the same number of neurons as number of features.
    Model is compiled with a specified loss function, optimizer, and metrics.

    Args:
        input_shape (tuple[int, ...]): input data's shape (timesteps, features).
        lstm_metrics (list[metrics]): metrics to use when compiling model.

    Returns:
        Sequential: compiled stacked LSTM model.
    """
    model = Sequential()

    # 1st masking layer: specify input shape.
    model.add(Masking(mask_value=PAD_VALUE, input_shape=input_shape))
    # 1st LSTM layer: specify input shape & return sequences.
    model.add(
        LSTM(
            LSTM_NEURONS[0],
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
            LSTM_NEURONS[1],
            activation=ACTIVATIONS[1],
            dropout=DROPOUT_RATE,
            recurrent_dropout=DROPOUT_RATE,
        )
    )

    model.add(Dense(input_shape[-1], activation=ACTIVATIONS[-1]))
    model.compile(
        loss=LOSS_FUNCTION,
        optimizer=optimizers.Adafactor(learning_rate=LEARNING_RATE),
        metrics=lstm_metrics,
    )

    return model
