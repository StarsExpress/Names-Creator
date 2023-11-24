"""All models configurations."""

# Deep learning training settings.
PAD_VALUE = -1  # Mask value for all padded timesteps.

UNITS_LIST = [80, 64]  # Neuron units for stacked recurrent networks.

ACTIVATIONS_LIST = ['softsign', 'tanh', 'softmax']  # Activation functions of recurrent and output layers.

DROPOUT_RATE = 0.2  # For both forward and backward propagations.

LOSS_FUNCTION = 'kl_divergence'

LEARNING_RATE = 0.025

EPOCHS = 100

DENOMINATOR = 4  # Divided by epochs as call back threshold.
