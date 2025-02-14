from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model, scaler, and label encoder
model = joblib.load('crop_model.pkl')  # Load the trained model
scaler = joblib.load('scaler.pkl')  # Load the saved scaler
le = joblib.load('label_encoder.pkl')  # Load the saved label encoder

# Function to predict the crop
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    scaled_features = scaler.transform(features)  # Scale the input
    prediction = model.predict(scaled_features)  # Predict
    return le.inverse_transform(prediction)[0]  # Convert back to label

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get input values from form
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Predict crop
        predicted_crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)

        return render_template('index.html', prediction=predicted_crop)  # Send prediction to frontend

    return render_template('index.html', prediction=None)  # Default page

if __name__ == '__main__':
    app.run(debug=True)
