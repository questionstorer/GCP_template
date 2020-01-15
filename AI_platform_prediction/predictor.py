from sklearn.externals import joblib
import os

class MyPredictor(object):
  def __init__(self, model, encoder):
    self._model = model
    self._encoder = encoder

  def predict(self, instances, **kwargs):

    preprocessed_inputs = self._encoder.transform(instances)


    return ["survive" if _==1 else "die" for _ in list(self._model.predict(preprocessed_inputs))]


  @classmethod
  def from_path(cls, model_dir):
    model_path = os.path.join(model_dir, 'titanic_model.joblib')
    model = joblib.load(model_path)

    encoder_path = os.path.join(model_dir, 'titanic_encoder.joblib')
    encoder = joblib.load(encoder_path)

    return cls(model, encoder)