#################### Files Required For Deployment #########################
# UI : implemented by Streamlit library
# Trained Model Files: Saved pkl files
# Logic Code connecting UI & Pkl files
############################################################################

# Importing required libraries
import streamlit as st
import pandas as pd
import sklearn
import warnings
warnings.filterwarnings('ignore')
import pickle

# Streamlit Page Configuration
st.set_page_config(
    page_title="Water Quality Index Prediction",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Customizing App Background and Title
st.markdown("<h1 style='text-align: center; color: DeepGold;'>🌟 Water Quality Index Prediction 🌟</h1>", unsafe_allow_html=True)


# Load Dataset for Reference
try:
    df = pd.read_csv("water_potability.csv")
    st.subheader("📊 Sample Data")
    st.dataframe(df.tail(), use_container_width=True)
except FileNotFoundError:
    st.error("❌ Error: 'water_potability.csv' file not found. Please upload the dataset.")
    st.stop()

# Load Trained Model
try:
    with open('water_rfc.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("❌ Error: 'water_naive.pkl' file not found. Please upload the trained model.")
    st.stop()

# User Input Section
st.subheader("📝 Input Water Quality Parameters")

input_columns = [
    "ph", "Hardness", "Solids", "Chloramines", "Sulfate",
    "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"
]

user_inputs = {}

for i in range(0, len(input_columns), 2):
    col1, col2 = st.columns(2)
    with col1:
        user_inputs[input_columns[i]] = st.number_input(
            f"Enter {input_columns[i]} Value (Min: {df[input_columns[i]].min():.2f}, Max: {df[input_columns[i]].max():.2f})",
            min_value=float(df[input_columns[i]].min()),
            max_value=float(df[input_columns[i]].max()),
            step=0.01
        )
    if i + 1 < len(input_columns):
        with col2:
            user_inputs[input_columns[i + 1]] = st.number_input(
                f"Enter {input_columns[i + 1]} Value (Min: {df[input_columns[i + 1]].min():.2f}, Max: {df[input_columns[i + 1]].max():.2f})",
                min_value=float(df[input_columns[i + 1]].min()),
                max_value=float(df[input_columns[i + 1]].max()),
                step=0.01
            )

# Prepare Input DataFrame
xdata = pd.DataFrame([user_inputs])
st.write("### Given Input:")
st.dataframe(xdata, use_container_width=True)

# Prediction Logic
if st.button("🔍 Predict"):
    prediction = model.predict(xdata)

    if prediction[0] == 0:
        st.markdown("<h1 style='text-align: center; color: red;'>❌ Water is Unsafe for Drinking</h1>",
                    unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center; color: blue;'>✅ Water is Safe for Drinking</h1>",
                    unsafe_allow_html=True)


