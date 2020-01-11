import logging
import tensorflow as tf
import metadata
import pandas as pd

def download(filename):
    # download file from Cloud Storage to local
    with tf.io.gfile.GFile(filename) as file_read:
        temp_filename = filename.split("/")[-1]
        with open(temp_filename, "w") as file_write:
            for line in file_read:
                line += '\n'
                file_write.write(line)
    return temp_filename
def create_dataset(args, filename, encoder):
    df = pd.read_csv(filename)
    df["text"] = df["text"].apply(lambda text: encoder.encode(text))
    df["label"] = df["label"].apply(lambda label: 0 if label <= 4 else 1)

    data_set = [(tf.constant(row[0]), tf.constant(row[1])) for row in df.itertuples(index=False)]

    def dataset_generator():
        for data in data_set:
            yield data

    dataset = tf.data.Dataset.from_generator(dataset_generator,
                                         (tf.int32, tf.int32),
                                         (tf.TensorShape([None]), tf.TensorShape(())))
    dataset = dataset.shuffle(10000)
    dataset = dataset.padded_batch(args.batch_size, dataset.output_shapes)
    return dataset