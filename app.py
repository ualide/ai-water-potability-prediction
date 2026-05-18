import streamlit as st
import pandas as pd
import sqlite3
import requests

# --- 1. Database Management ---
def init_db():
    conn = sqlite3.connect('water_quality.db')
    c = conn.cursor()

    # إنشاء table إذا ماكانش
    c.execute('''
    CREATE TABLE IF NOT EXISTS predictions_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ph REAL,
        hardness REAL,
        solids REAL,
        chloramines REAL,
        sulfate REAL,
        conductivity REAL,
        organic REAL,
        trihalo REAL,
        turbidity REAL,
        result TEXT,
        confidence REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()


def save_to_db(data, result, confidence):
    try:
        conn = sqlite3.connect('water_quality.db')
        c = conn.cursor()

        values = (
            float(data["ph"]),
            float(data["Hardness"]),
            float(data["Solids"]),
            float(data["Chloramines"]),
            float(data["Sulfate"]),
            float(data["Conductivity"]),
            float(data["Organic_carbon"]),
            float(data["Trihalomethanes"]),
            float(data["Turbidity"]),
            result,
            float(confidence)
        )

        c.execute("""
        INSERT INTO predictions_history 
        (ph, hardness, solids, chloramines, sulfate, conductivity, organic, trihalo, turbidity, result, confidence)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, values)

        conn.commit()
        conn.close()
        return True

    except Exception as e:
        st.error(f"Database Error: {e}")
        return False


# --- INIT DB ---
init_db()

# --- 2. Page Config ---
st.set_page_config(page_title="Water Quality AI", layout="wide")
st.title("💧 Smart Water Monitoring System")

# --- 3. Sidebar ---
st.sidebar.header("📂 Data Loading")
auto_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if auto_file:
    df = pd.read_csv(auto_file).fillna(0)
    idx = st.sidebar.number_input("Row Index", 0, len(df)-1, 0)

    if st.sidebar.button("⚡ Load Row"):
        st.session_state.row_data = df.iloc[idx]

row = st.session_state.get('row_data', None)

# --- 4. Inputs ---
st.header("🔮 Analysis")
col1, col2, col3 = st.columns(3)

def get_v(key, default):
    return float(row[key]) if row is not None else default

with col1:
    ph = st.number_input("pH", value=get_v('ph', 7.0))
    hard = st.number_input("Hardness", value=get_v('Hardness', 150.0))
    sol = st.number_input("Solids", value=get_v('Solids', 20000.0))

with col2:
    chl = st.number_input("Chloramines", value=get_v('Chloramines', 7.0))
    sul = st.number_input("Sulfate", value=get_v('Sulfate', 300.0))
    con = st.number_input("Conductivity", value=get_v('Conductivity', 400.0))

with col3:
    org = st.number_input("Organic Carbon", value=get_v('Organic_carbon', 10.0))
    tri = st.number_input("Trihalomethanes", value=get_v('Trihalomethanes', 60.0))
    tur = st.number_input("Turbidity", value=get_v('Turbidity', 4.0))

inputs = {
    "ph": ph,
    "Hardness": hard,
    "Solids": sol,
    "Chloramines": chl,
    "Sulfate": sul,
    "Conductivity": con,
    "Organic_carbon": org,
    "Trihalomethanes": tri,
    "Turbidity": tur
}

# --- 5. Action ---
if st.button("🚀 Analyze via API"):
    try:
        res = requests.post("http://127.0.0.1:9000/predict", json=inputs)

        if res.status_code == 200:
            data = res.json()
            label = data['label']
            conf = data['confidence']

            if label == "Drinkable":
                st.success(f"### Result: {label}")
            else:
                st.error(f"### Result: {label}")

            st.metric("Confidence", f"{conf*100:.2f}%")

            # 💾 Save
            if save_to_db(inputs, label, conf):
                st.toast("Saved to Database!")

        else:
            st.error("❌ Check API (main.py)")

    except Exception as e:
        st.error(f"Error: {e}")

# --- 6. History ---
st.divider()

if st.checkbox("📜 Show History"):
    try:
        conn = sqlite3.connect('water_quality.db')
        df_hist = pd.read_sql_query(
            "SELECT * FROM predictions_history ORDER BY id DESC",
            conn
        )
        st.dataframe(df_hist, use_container_width=True)
        conn.close()

    except Exception as e:
        st.error(f"Error loading history: {e}")