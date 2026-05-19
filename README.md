Project Overview
AI Water Potability Prediction is a Python-based machine learning project developed for the Python module. The main goal of this project is to predict whether water is drinkable or not based on different physicochemical parameters.
The system uses a trained machine learning model to analyze water quality data and return a prediction with a confidence score. The project also includes a Streamlit dashboard, a FastAPI backend, and a SQLite database to store prediction history.

Team Members
•	Oualid Ouarrach
•	Mahmoud Charabara
•	Youness Eziddy
•	Imad Addioui

Supervisor
Prof. Yassine Oukdach

Modul
Python

Program
Master Ingénierie Informatique et Systèmes Embarqués

Project Features
•	Upload water quality CSV data
•	Select a specific row from the dataset
•	Analyze water quality using a trained machine learning model
•	Predict whether the water is Drinkable or Not Drinkable
•	Display prediction confidence
•	Store prediction history in a SQLite database
•	View previous predictions through the dashboard

Technologies Used
•	Python
•	FastAPI
•	Uvicorn
•	Streamlit
•	Scikit-learn
•	Pandas
•	NumPy
•	SQLite
•	Pickle
•	GitHub

Project Structure
ai-water-potability-prediction/
|
|-- Frontend/
|-- app.py
|-- main.py
|-- model.py
|-- train.py
|-- water_quality.py
|-- model.pkl
|-- scaler.pkl
|-- water_potability.csv
|-- water_quality.db
|-- Presentation.pptx
|-- Project_Report.pdf
|-- requirements.txt
|-- README.md
|-- LICENSE
|-- package.json
|-- package-lock.json

Dataset Description
The dataset contains several water quality parameters used to predict water potability:
•	pH
•	Hardness
•	Solids
•	Chloramines
•	Sulfate
•	Conductivity
•	Organic Carbon
•	Trihalomethanes
•	Turbidity
•	Potability
The target variable is Potability, which indicates whether the water is safe to drink or not.

How to Run the Project
1. Install Requirements
First, install the required Python libraries:
pip install -r requirements.txt

2. Run the Backend API
Open a terminal and run:
cd "C:\Users\PC\Desktop\M1 - IISE - S2\Python\Projet Python\water-quality-project"
python -m uvicorn main:app --port 9000 --reload

The backend will run on:
http://127.0.0.1:9000

3. Run the Streamlit Frontend
Open another terminal and run:
cd "C:\Users\PC\Desktop\M1 - IISE - S2\Python\Projet Python\water-quality-project"
python -m streamlit run app.py

The frontend dashboard will open on:
http://localhost:8501

Application Workflow
1.	The user uploads the water_potability.csv dataset.
2.	The user selects a row index from the dataset.
3.	The selected water quality values are loaded into the dashboard.
4.	The user clicks on the analysis button.
5.	The frontend sends the values to the FastAPI backend.
6.	The backend uses the trained model and scaler to make a prediction.
7.	The result is displayed as Drinkable or Not Drinkable.
8.	The prediction is stored in the SQLite database.

Database
The project uses a SQLite database named:
water_quality.db

The database stores prediction history in the predictions_history table, including:
•	Water quality parameters
•	Prediction result
•	Confidence score
•	Prediction date and time

GitHub Repository
https://github.com/ualide/ai-water-potability-prediction

Conclusion
This project helped us apply Python programming, data preprocessing, machine learning, API development, frontend design, and database management in one complete application. It demonstrates how artificial intelligence can be used to support water quality monitoring and decision-making.
