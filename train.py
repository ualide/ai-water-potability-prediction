import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Load Data
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "water_potability.csv")

data = pd.read_csv(csv_path)

# 2. Handling Missing Values (أهم مرحلة فصلاحية الماء)
# كاينين قيم ناقصة بزاف ف Sulfate و pH، التعويض بالمتوسط كيعاون الموديل
data.fillna(data.mean(), inplace=True)

X = data.drop("Potability", axis=1)
y = data["Potability"]

# 3. Scaling (تحويل المقاييس)
# استعملنا StandardScaler باش نرجعو كاع الأرقام فتقارب واحد
scaler = StandardScaler()
# كنحتفظ بأسماء الأعمدة باش نتفادو الـ Warning فـ app.py
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# 4. Split Data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 5. Model Training (تحسين المعايير)
# زدت n_estimators (عدد الأشجار) و random_state باش تكون النتيجة مستقرة
model = RandomForestClassifier(n_estimators=200, max_depth=15, random_state=42)
model.fit(X_train, y_train)

# 6. Check Accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc * 100:.2f}%")

# 7. Save Model & Scaler
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))