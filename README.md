🧠 Mental Well-Being Prediction Using Machine Learning
📌 Project Overview

This project focuses on predicting an individual’s mental well-being using machine learning techniques based on lifestyle and behavioral data. The system analyzes daily habits such as sleep, stress, screen time, exercise, and social interaction to classify mental well-being into meaningful psychological categories.

The project follows a complete predictive analytics pipeline, including data collection, preprocessing, exploratory data analysis (EDA), model development, evaluation, and deployment through an interactive web application.

🎯 Mental Well-Being Categories

The model classifies mental well-being into the following categories:

Psychological Strain

Adaptive Coping

Psychological Flourishing

These categories are designed to provide interpretable and psychologically meaningful insights rather than generic labels.

📂 Dataset

Source: Primary data collected using a Google Form survey

Data Type: Lifestyle and behavioral attributes

Enhancement: Controlled synthetic data generation was used to balance the dataset while maintaining realistic feature relationships

Target Variable: Overall mental well-being score/category

Key Features

Age

Sleep hours

Screen time

Water intake

Exercise frequency

Work/study hours

Break frequency

Multitasking behavior

Stress level

Social interaction time

Relationship quality

Hobbies

🔍 Exploratory Data Analysis (EDA)

EDA was performed to understand feature distributions and relationships, including:

Distribution analysis of numerical features using histograms

Correlation analysis between lifestyle factors and mental well-being

Feature importance analysis using Random Forest

These insights helped guide feature selection and model choice.

🤖 Machine Learning Models Used

The following classification models were implemented and compared:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier ✅ (Best-performing model)

K-Nearest Neighbors (KNN)

📊 Model Evaluation Metrics

Models were evaluated using multiple performance metrics:

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

Random Forest demonstrated the most balanced and robust performance across all metrics.

🌳 Feature Importance

Feature importance analysis using Random Forest highlighted key factors influencing mental well-being, including:

Stress level

Sleep duration

Screen time

Exercise frequency

Social interaction

This improves model interpretability and provides actionable insights.

💻 Web Application (Streamlit)

An interactive web application was developed using Streamlit that allows users to:

Enter lifestyle details in a survey-like format

Receive instant mental well-being predictions

Get personalized feedback for improving mental health

The interface uses a clean, light theme for better readability and user experience.

🛠️ Technologies Used

Programming Language: Python

Libraries:

Pandas

NumPy

Matplotlib

Scikit-learn

Streamlit

Tools:

Jupyter Notebook

VS Code

GitHub
📈 Project Highlights

End-to-end machine learning workflow

Real-world primary dataset

Model comparison and evaluation

Explainable feature importance

User-centric prediction and feedback system

🔮 Future Scope

Integration with wearable devices for real-time data

Cloud deployment for scalability

Mobile application development

Use of advanced deep learning models

Continuous mental well-being tracking

👨‍🎓 Author

Rajinder Singh
B.Tech (Data Science)
Machine Learning & Predictive Analytics Project

📜 License

This project is intended for academic and educational purposes.
