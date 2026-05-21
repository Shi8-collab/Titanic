Titanic Survival Prediction 🚢

A Machine Learning project that predicts whether a passenger survived the Titanic disaster using classification algorithms. This project includes model training, preprocessing, and deployment-ready files like app.py, requirements.txt, and saved model pipeline.

📌 Features
Titanic survival prediction
Machine Learning pipeline using Scikit-learn
Data preprocessing included
Model saved using Joblib/Pickle
Simple and beginner-friendly project
Ready for deployment on Hugging Face Spaces
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
Streamlit / Gradio (if used)
📂 Project Structure
├── app.py
├── requirements.txt
├── survival_check.pkl
├── Titanic-Dataset.csv
└── README.md
📊 Input Features

The model predicts survival based on features like:

Passenger Class (Pclass)
Gender
Age
Fare
SibSp
Parch
🚀 How to Run the Project
1️⃣ Clone Repository
git clone https://github.com/your-username/titanic-survival-prediction.git
cd titanic-survival-prediction
2️⃣ Install Requirements
pip install -r requirements.txt
3️⃣ Run Application
python app.py

or if using Streamlit:

streamlit run app.py
🧠 Machine Learning Model

Algorithms that can be used:

Logistic Regression
Random Forest Classifier
Decision Tree
Support Vector Machine (SVM)
📈 Model Accuracy

Example accuracy achieved:

Accuracy: 85%+

(Replace with your actual accuracy)

💾 Saved Model

The trained model is stored as:

survival_check.pkl

It can be loaded using:

import joblib

model = joblib.load("survival_check.pkl")
🌐 Deployment

You can deploy this project on:

Hugging Face Spaces
Render
Railway
Streamlit Cloud
📸 Project Preview

Add screenshots here after deployment.

👩‍💻 Author

Shivani Kumari

⭐ GitHub

If you like this project, give it a ⭐ on GitHub.
