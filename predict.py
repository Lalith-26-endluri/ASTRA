import tensorflow as tf
import numpy as np

# Try loading trained model
try:
    model = tf.keras.models.load_model("risk_model.h5")
except:
    model = None

def predict_risk(crowd_count):

    if model:
        input_data = np.array([[crowd_count]])
        risk_score = model.predict(input_data)[0][0]
    else:
        # Simple fallback logic
        risk_score = min(crowd_count / 100, 1.0)

    return float(risk_score)
