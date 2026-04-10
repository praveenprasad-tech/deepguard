import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

# Load pretrained model
model = MobileNetV2(weights="imagenet")

def predict(image):
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)

    preds = model.predict(image)
    result = decode_predictions(preds, top=1)[0][0][1]

    return result