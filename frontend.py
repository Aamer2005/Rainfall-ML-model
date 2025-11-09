import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# App title
st.title("🌦️ Weather Prediction using Logistic Regression")

st.write("Enter the input values below and click **Predict** to get the model's output.")

# Create input fields for all 11 features
day = st.number_input("Day", min_value=1, max_value=366, value=328)
pressure = st.number_input("Pressure (hPa)", value=1019.7)
maxtemp = st.number_input("Max Temperature (°C)", value=23.2)
temperature = st.number_input("Temperature (°C)", value=20.9)
mintemp = st.number_input("Min Temperature (°C)", value=18.6)
dewpoint = st.number_input("Dew Point (°C)", value=16.8)
humidity = st.number_input("Humidity (%)", value=75.0)
cloud = st.number_input("Cloud (%)", value=88.0)
sunshine = st.number_input("Sunshine (hours)", value=0.0)
winddirection = st.number_input("Wind Direction (°)", value=30.0)
windspeed = st.number_input("Wind Speed (km/h)", value=38.3)

# When the user clicks the button
if st.button("Predict"):
    # Prepare the input array (11 features)
    input_data = np.array([[day, pressure, maxtemp, temperature, mintemp,
                            dewpoint, humidity, cloud, sunshine, winddirection, windspeed]])

    # Make prediction
    from sklearn.preprocessing import StandardScaler
    test_scaled_df = scaler.transform(input_data)
    prediction = model.predict(test_scaled_df)
    y_pred = model.predict_proba(test_scaled_df)[:,1]

    # Display result
    # st.success(f"✅ Prediction: {prediction[0]}")
    st.success(f"✅ Prediction: {y_pred[:]}")