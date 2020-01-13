import logging
import tensorflow as tf
import tensorflow_datasets as tfds

def _corpus_generator(filename):

    def generator():
        with open(filename) as file:
            for row in file:
                yield row
    return generator()

def create_encoder(args, textonly_file):
    # create subword encoder
    encoder = tfds.features.text.SubwordTextEncoder.build_from_corpus(
        _corpus_generator(textonly_file), target_vocab_size=args.vocab_size)
    return encoder

def create_keras_model(args):
  # model contain four layers
  hidden_units = [int(size) for size in args.hidden_units.split()]

  model = tf.keras.Sequential([
      tf.keras.layers.Embedding(args.vocab_size, hidden_units[0]),
      tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(hidden_units[1])),
      tf.keras.layers.Dense(hidden_units[2], activation='relu'),
      tf.keras.layers.Dense(hidden_units[3], activation='sigmoid')
  ])
  model.compile(loss='binary_crossentropy',
                optimizer=tf.keras.optimizers.Adam(args.learning_rate),
                metrics=['accuracy'])
  return model