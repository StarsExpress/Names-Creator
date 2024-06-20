"""All models configurations."""

# Deep learning training settings.
PAD_VALUE = -1  # Mask value for all padded timesteps.

LSTM_NEURONS = [80, 64]  # Stacked LSTM.

ACTIVATIONS = [
    "softsign",
    "tanh",
    "softmax",
]  # Recurrent & output layers.

DROPOUT_RATE = 0.2  # Both forward & backward propagations.

LOSS_FUNCTION = "kl_divergence"

LEARNING_RATE = 0.025

EPOCHS = 100

DENOMINATOR = 4  # Call back threshold = epochs // denominator .
