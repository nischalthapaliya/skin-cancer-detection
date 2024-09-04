from flask import Flask, request, render_template, redirect, url_for
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load your trained model
MODEL_PATH = 'models/model_densenet.h5'
model = load_model(MODEL_PATH)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)
            
            # Predict
            img = image.load_img(filepath, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0
            pred = model.predict(img_array)
            predicted_class = np.argmax(pred, axis=1)
            label = 'Benign' if predicted_class[0] == 0 else 'Malignant'
            
            return label
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
