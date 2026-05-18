import pandas as pd

# قراءة ملف CSV
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "water_potability.csv")

data = pd.read_csv(file_path)

print(data.head())

# عرض أول 5 سطور
print(data.head())