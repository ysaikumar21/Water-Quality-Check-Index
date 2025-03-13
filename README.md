**Water Quality Check Index 🌊💧**

**AI-Powered Water Quality Classification Using Machine Learning & Streamlit**

📌 Overview
This project leverages machine learning and data analytics to classify water quality based on various physicochemical parameters. The model predicts contamination levels and provides actionable insights for environmental monitoring and public health safety.

🚀 Features
Machine Learning Model: Utilizes Random Forest, SVM, and XGBoost for high-accuracy classification.
Data Preprocessing & Feature Engineering: Implements scaling, normalization, and missing value imputation to enhance model performance.
Real-time Dashboard: Deployed using Streamlit, enabling interactive water quality assessment and visualization.
Predictive Analytics: Helps in early detection of contamination and assists decision-making for regulatory bodies.
Automated Pipeline: Seamless ETL (Extract, Transform, Load) process ensuring data consistency and efficiency.

📊 Dataset & Parameters
Dataset: 

Key Features:
pH Level – Measures acidity/alkalinity
Dissolved Oxygen (DO) – Essential for aquatic life
Turbidity – Indicates water clarity
Total Dissolved Solids (TDS) – Measures mineral content
Biochemical Oxygen Demand (BOD) – Determines organic pollution levels

🛠️ Tech Stack
Programming: Python 🐍
Libraries: Pandas, NumPy, Scikit-learn, TensorFlow, Matplotlib, Seaborn
Machine Learning Models: Random Forest, XGBoost, SVM
Deployment: Streamlit 🌐

📂 Project Structure

📁 Water-Quality-Check-Index  
│── 📂 data/                   # Raw & Processed Data  
│── 📂 models/                 # Trained Machine Learning Models  
│── 📂 scripts/                # Data Preprocessing & Training Scripts  
│── app.py                     # Streamlit Dashboard  
│── requirements.txt           # Dependencies  
│── README.md                  # Project Documentation  

⚡ Installation & Usage

Clone this repository:
git clone https://github.com/ysaikumar21/Water-Quality-Check-Index.git

cd Water-Quality-Check-Index

Install dependencies:
pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

Real time outputs of deployment link is :
https://water-quality-check-index-7.streamlit.app/

📈 Results & Insights
The trained model achieved high accuracy in water quality classification, effectively distinguishing between safe, moderately contaminated, and highly contaminated water samples. The Streamlit dashboard provides real-time insights for users, making it a practical tool for water resource management and environmental monitoring.
