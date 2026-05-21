import gradio as gr
import joblib
import pandas as pd

# Load model
model = joblib.load("survival_check.pkl")

# Prediction function
def predict_survival(Pclass, SibSp, Parch, Fare):

    data = pd.DataFrame({
        'Pclass': [Pclass],
        'SibSp': [SibSp],
        'Parch': [Parch],
        'Fare': [Fare]
    })

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1] * 100

    if prediction == 1:
        return f"Passenger Survived ✅\nChance of Survival: {probability:.2f}%"
    else:
        return f"Passenger Did Not Survive ❌\nChance of Survival: {probability:.2f}%"

# Interface
interface = gr.Interface(
    fn=predict_survival,

    inputs=[
        gr.Slider(1, 3, step=1, label="Passenger Class"),
        gr.Slider(0, 10, step=1, label="Siblings/Spouses"),
        gr.Slider(0, 10, step=1, label="Parents/Children"),
        gr.Number(label="Fare")
    ],

    outputs="text",

    title="🚢 Titanic Survival Prediction",

    description="Predict whether a passenger survived the Titanic disaster using Machine Learning.",

    examples=[
        [1, 1, 0, 80],
        [3, 0, 0, 10],
        [2, 1, 1, 30]
    ],

    theme=gr.themes.Soft()
)

interface.launch()