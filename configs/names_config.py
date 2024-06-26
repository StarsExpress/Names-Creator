"""All names configurations."""

import string


# Embeddings settings.
LOWER_CASE_LIST = list(string.ascii_lowercase)
UPPER_CASE_LIST = list(string.ascii_uppercase)
AUX_CHARS_DICT = {"start": "~", "end": "#"}  # Help embeddings.

# Sequence window = last-n characters to trace in sequences encoding.
# When window = 3, sequences encoding of 'Jack' gives: J, Ja, Jac and ack.
SEQUENCE_WINDOW = 4


# Creation settings.
MAX_FORENAME_LEN = 10
MAX_SURNAME_LEN = 10
