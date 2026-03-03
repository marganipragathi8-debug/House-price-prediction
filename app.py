import streamlit as st
import pickle
import numpy as np

#title
st.title("🏡💰House Price Prediction App")
st.write("This app predicts the price of a house based on its features.")
#load the model and scaling
with open("house_price_prediction.pkl", "rb") as f:
    model = pickle.load(f)
with open("scaling.pkl", "rb") as f:
    scaling = pickle.load(f)

#input features
Area = st.number_input("Enter the area of the house in square feet", min_value=0)
Bedrooms = st.number_input("Enter the number of bedrooms", min_value=0)
Bathrooms = st.number_input("Enter the number of bathrooms", min_value=0)
Floors = st.number_input("Enter the number of floors", min_value=0)
YearBuilt = st.number_input("Enter the year the house was built", min_value=1900)
DistanceToCity = st.number_input("Enter the distance to the city center in miles", min_value=0.0)
LocationScore = st.number_input("Enter the location score (1-10)", min_value=1, max_value=10)

#predict button
if st.button("Predict Price"):
    #get the input values
    prediction_input =np.array([[Area, Bedrooms, Bathrooms, Floors, YearBuilt, DistanceToCity, LocationScore]])
    #scale the input features
    scaled_input=scaling.transform(prediction_input)
    #make the prediction
    predicted_price=model.predict(scaled_input)
    st.write(f"The predicted price of the house is: ${predicted_price[0]:,.2f}")