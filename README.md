
# **Weather Prediction using Logistic Regression**

## **Members Information**

| Name of Student | Roll No. | Role / Work Done |
|-----------------|-----------|------------------|
| Mohammed Aamer | 2023BIT064 | Data preprocessing, model training,Streamlit web application development,model integration ,and documentation  |
| Mane Rohan | 2023BIT025 | Data analysis,model training, hyperparameter tuning, model integration,model evaluation, and deployment , documentation |

## **Project Description**

This project implements a **machine learning system** to predict rainfall probability based on meteorological data. Using a **Logistic Regression** model, the system analyzes various weather parameters to classify whether rainfall is likely to occur.

### **Key Features:**
- **Machine Learning Model**: Logistic Regression with hyperparameter tuning
- **Web Interface**: Streamlit-based web application for real-time predictions
- **Data Preprocessing**: StandardScaler for feature normalization
- **Model Performance**: Achieved 92.17% ROC-AUC score on test data

### **Technologies & Algorithms Used:**
- **Programming Language**: Python
- **Machine Learning**: Scikit-learn (Logistic Regression, StandardScaler, GridSearchCV)
- **Web Framework**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Model Persistence**: Joblib

### **Input Features:**
The model uses 11 meteorological parameters to make predictions:
- Day of the year
- Atmospheric pressure
- Maximum temperature
- Current temperature
- Minimum temperature
- Dew point
- Humidity
- Cloud cover
- Sunshine hours
- Wind direction
- Wind speed

### **Project Structure:**
- `model_copy.ipynb` - Jupyter notebook containing data analysis, model training, and evaluation
- `frontend_copy.py` - Streamlit web application for user interaction
- `model2.pkl` - Serialized trained model
- `scaler2.pkl` - Serialized scaler for data preprocessing
- `train.csv` - Training dataset
- `test.csv` - Test dataset

### **How to Use:**
1. Run the Streamlit app: `streamlit run frontend_copy.py`
2. Input weather parameters in the web interface
3. Click "Predict" to get rainfall probability
4. The model returns a probability score between 0-1 indicating likelihood of rainfall

The project demonstrates end-to-end machine learning workflow from data preparation to model deployment, providing an intuitive interface for weather prediction tasks.

---