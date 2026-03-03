# 🏠 House Price Prediction App

A machine learning web application built with **Streamlit** that predicts house prices based on key features using a **Linear Regression** model.

🔴 **Live App:** [Click here to try the app!](https://house-price-prediction-j8w9wjfelzdbrxicodhsdp.streamlit.app/)

---

## 📌 Project Overview

This project uses a dataset of 20,000 house records to train a Linear Regression model that predicts the price of a house based on input features such as area, number of bedrooms, bathrooms, floors, year built, distance to city, and location score.

---

## 🚀 Live Demo

👉 [https://house-price-prediction-j8w9wjfelzdbrxicodhsdp.streamlit.app/](https://house-price-prediction-j8w9wjfelzdbrxicodhsdp.streamlit.app/)

Enter your house details and instantly get a predicted price!

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| Python 3 | Core programming language |
| Streamlit | Interactive web application |
| Scikit-learn | Linear Regression model & scaling |
| Pandas & NumPy | Data manipulation |
| Matplotlib & Seaborn | Data visualization |
| Pickle | Model serialization |
| Jupyter Notebook | EDA & model training |

---

## 📁 Project Structure

```
House-price-prediction/
│
├── House_Price_prediction.ipynb   # EDA + model training notebook
├── app.py                         # Streamlit web application
├── house_price_20k_dataset.csv    # Dataset (20,000 records)
├── house_price_prediction.pkl     # Trained Linear Regression model
├── scaling.pkl                    # StandardScaler for input features
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## 🧠 Model Details

- **Algorithm:** Linear Regression
- **Dataset:** 20,000 house records
- **Input Features:**
  - 📐 Area (square feet)
  - 🛏️ Number of Bedrooms
  - 🚿 Number of Bathrooms
  - 🏢 Number of Floors
  - 📅 Year Built
  - 📍 Distance to City Center (miles)
  - ⭐ Location Score (1-10)
- **Output:** Predicted House Price (USD)

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/marganipragathi8-debug/House-price-prediction.git
cd House-price-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```

### 4. Open in browser
```
http://localhost:8501
```

---

## 📋 Requirements

```
streamlit
numpy
scikit-learn
pandas
```

---

## 📈 Project Workflow

1. **Data Collection** - 20,000 house records dataset
2. **Exploratory Data Analysis (EDA)** - Understanding patterns & distributions
3. **Data Preprocessing** - Feature scaling using StandardScaler
4. **Model Training** - Linear Regression model
5. **Model Evaluation** - R², MAE, RMSE metrics
6. **Deployment** - Streamlit web app hosted on Streamlit Cloud

---

## 🙋‍♀️ Author

**Pragathi Margani**
- GitHub: [@marganipragathi8-debug](https://github.com/marganipragathi8-debug)
- Live App: [House Price Prediction](https://house-price-prediction-j8w9wjfelzdbrxicodhsdp.streamlit.app/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
