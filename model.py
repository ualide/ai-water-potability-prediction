import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1️⃣ Load dataset
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "water_potability.csv")

data = pd.read_csv(csv_path)

# 2️⃣ Handle missing values
data.fillna(data.mean(), inplace=True)

# 3️⃣ Features & target
X = data.drop("Potability", axis=1)
y = data["Potability"]

# 4️⃣ Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 5️⃣ Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 6️⃣ Model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# 7️⃣ Prediction
y_pred = model.predict(X_test)

# 8️⃣ Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 9️⃣ Test one sample prediction
sample = X_test[0].reshape(1, -1)
result = model.predict(sample)

if result[0] == 1:
    print("💧 Water is POTABLE (Safe to drink)")
else:
    print("☠ Water is NOT POTABLE (Unsafe)")