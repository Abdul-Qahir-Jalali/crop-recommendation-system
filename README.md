# Crop Recommendation System

## Overview
The **Crop Recommendation System** is a machine learning-based web application designed to assist farmers and agricultural experts in making informed decisions about crop selection. By analyzing key soil and environmental parameters, the system predicts the most suitable crop to cultivate, thereby optimizing yield and resource usage.

The application is built using **Flask** for the backend and **scikit-learn** for the machine learning model. It provides a user-friendly interface where users can input environmental data and receive instant crop recommendations.

## Features
- **Accurate Predictions**: Uses a trained machine learning model to predict crops based on scientific data.
- **User-Friendly Interface**: Simple and intuitive web form for entering data.
- **Real-Time Results**: Instant processing of inputs to display recommendations.
- **Comprehensive Parameters**: Considers 7 distinct environmental and soil factors:
    - **Nitrogen (N)**: Ratio of Nitrogen content in soil.
    - **Phosphorus (P)**: Ratio of Phosphorus content in soil.
    - **Potassium (K)**: Ratio of Potassium content in soil.
    - **Temperature**: Temperature in degree Celsius.
    - **Humidity**: Relative humidity in %.
    - **pH**: pH value of the soil.
    - **Rainfall**: Rainfall in mm.

## Technologies Used
- **Programming Language**: Python
- **Web Framework**: Flask (v3.1.0)
- **Machine Learning**: scikit-learn (v1.6.1), joblib (v1.4.2), numpy (v1.26.4)
- **WSGI Server**: Gunicorn (v21.2.0)
- **Frontend**: HTML (Jinja2 templates)

## Project Structure
```
crop/
├── .git/                   # Git repository metadata
├── templates/              # HTML templates for the web interface
│   └── index.html          # Main application page
├── app.py                  # Main Flask application logic
├── crop_model.pkl          # Trained machine learning model
├── label_encoder.pkl       # Label encoder for decoding prediction tags
├── predict.py              # Script for testing prediction logic
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python runtime configuration
├── scaler.pkl              # Scaler for normalizing input features
└── wsgi.py                 # WSGI entry point for deployment
```

## Installation
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Abdul-Qahir-Jalali/crop-recommendation-system.git
   cd crop-recommendation-system
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Start the application**:
   ```bash
   python app.py
   ```
   Or using Gunicorn:
   ```bash
   gunicorn wsgi:app
   ```

2. **Access the interface**:
   Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. **Get a Recommendation**:
   - Fill in the values for Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall.
   - Click the "Predict" button.
   - The recommended crop will be displayed on the screen.

## Model Information
The core prediction engine uses a pre-trained machine learning model (`crop_model.pkl`).
- **Input Scaling**: Data is pre-processed using `scaler.pkl` to ensure accurate predictions.
- **Output Decoding**: The model's numeric output is converted back to readable crop names using `label_encoder.pkl`.

## Deployment
This application is configured for deployment on platforms like Render or Heroku using `gunicorn` and `wsgi.py`.
