from keras.models import Sequential
from keras.layers import Embedding, Bidirectional, LSTM
from keras_contrib.layers import CRF


EMBED_DIM = 100
BiRNN_UNITS = 200


model = Sequential()
model.add(Embedding(len(vocab), EMBED_DIM, mask_zero=True))  # Random embedding
model.add(Bidirectional(LSTM(BiRNN_UNITS // 2, return_sequences=True)))
crf = CRF(len(chunk_tags), sparse_target=True)
model.add(crf)
model.summary()
model.compile('adam', loss=crf.loss_function, metrics=[crf.accuracy])

