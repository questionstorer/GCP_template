from sklearn.externals import joblib
import numpy as np
import os

class MyPredictor(object):
  def __init__(self, model, encoder):
    self._model = model
    self._encoder = encoder

  def predict(self, instances, **kwargs):

    preprocessed_inputs = self._encoder.transform(instances)


    return list(self._model.predict(preprocessed_inputs))


  @classmethod
  def from_path(cls, model_dir):
    model_path = os.path.join(model_dir, 'titanic.joblib')
    model = joblib.load(model_path)

    encoder_path = os.path.join(model_dir, 'input_encoder.joblib')
    encoder = joblib.load(encoder_path)

    return cls(model, encoder)