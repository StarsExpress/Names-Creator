"""All models configurations."""

# Deep learning training settings.
PAD_VALUE = -1  # Mask value for all padded timesteps.

NEURONS_UNITS = [80, 64]  # Stacked recurrent networks.

ACTIVATIONS = [
    "softsign",
    "tanh",
    "softmax",
]  # Recurrent and output layers.

DROPOUT_RATE = 0.2  # Both forward and backward propagations.

LOSS_FUNCTION = "kl_divergence"

LEARNING_RATE = 0.025

EPOCHS = 100

DENOMINATOR = 4  # Divided by epochs as call back threshold.
