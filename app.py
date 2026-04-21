# import streamlit as st
# import joblib
# import pandas as pd
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="AgriPrice AI", page_icon="🌾", layout="wide")

# # Load files
# model = joblib.load("model.pkl")
# crop_encoder = joblib.load("crop_encoder.pkl")
# city_encoder = joblib.load("city_encoder.pkl")

# # Title
# st.title("🌾 AgriPrice AI")
# st.subheader("Smart Crop Price Prediction & Market Comparison")

# st.sidebar.header("Inputs")

# crop = st.sidebar.selectbox("Select Crop", crop_encoder.classes_)
# city = st.sidebar.selectbox("Select City", city_encoder.classes_)
# month = st.sidebar.slider("Select Month", 1, 12, 6)

# crop_val = crop_encoder.transform([crop])[0]
# city_val = city_encoder.transform([city])[0]

# # Prediction
# pred = model.predict([[month, crop_val, city_val]])[0]

# # Compare all cities
# results = []

# for c in city_encoder.classes_:
#     c_val = city_encoder.transform([c])[0]
#     p = model.predict([[month, crop_val, c_val]])[0]
#     results.append([c, round(p, 2)])

# df = pd.DataFrame(results, columns=["City", "Predicted Price"])

# best_city = df.loc[df["Predicted Price"].idxmax(), "City"]
# best_price = df["Predicted Price"].max()

# # Top Cards
# col1, col2 = st.columns(2)

# with col1:
#     st.metric("Predicted Price", f"Rs {pred:.2f}")

# with col2:
#     st.metric("Best City", f"{best_city} (Rs {best_price:.2f})")

# # Table
# st.write("## 📊 City Comparison Table")
# st.dataframe(df, use_container_width=True)

# # ------------------------------
# # GRAPH 1 Multi Line Trends
# # ------------------------------
# st.write("## 📈 Trend of Selected Crop in All Cities")

# fig1, ax1 = plt.subplots(figsize=(12,6))

# colors = ['blue','green','red','orange','purple']

# for i, c in enumerate(city_encoder.classes_):
#     c_val = city_encoder.transform([c])[0]
#     months = list(range(1,13))
#     prices = []

#     for m in months:
#         p = model.predict([[m, crop_val, c_val]])[0]
#         prices.append(p)

#     ax1.plot(months, prices, marker='o', linewidth=2.5,
#              label=c, color=colors[i])

# ax1.set_title(f"{crop} Price Trend Across Cities")
# ax1.set_xlabel("Month")
# ax1.set_ylabel("Price")
# ax1.legend()
# ax1.grid(True)

# st.pyplot(fig1)

# # ------------------------------
# # GRAPH 2 Dynamic Current Month
# # ------------------------------
# st.write("## 🌍 Current Month Comparison")

# fig2, ax2 = plt.subplots(figsize=(12,6))

# bars = ax2.bar(df["City"], df["Predicted Price"],
#                color=['blue','green','red','orange','purple'])

# for bar in bars:
#     y = bar.get_height()
#     ax2.text(bar.get_x()+bar.get_width()/2, y+10,
#              f'{y:.0f}', ha='center')

# ax2.set_title(f"{crop} Prices in Month {month}")
# ax2.set_xlabel("City")
# ax2.set_ylabel("Price")

# st.pyplot(fig2)

# st.caption("Machine Learning Based Decision Support System")




# import streamlit as st
# import joblib
# import pandas as pd
# import matplotlib.pyplot as plt

# # --------------------------
# # PAGE CONFIG
# # --------------------------
# st.set_page_config(
#     page_title="AgriPrice AI",
#     page_icon="🌾",
#     layout="wide"
# )

# # --------------------------
# # CUSTOM STYLE
# # --------------------------
# st.markdown("""
# <style>
# .metric-box{
#     padding:15px;
#     border-radius:12px;
#     background:#eaf7ea;
#     border:1px solid #cceccc;
# }
# .small{
#     font-size:14px;
#     color:gray;
# }
# </style>
# """, unsafe_allow_html=True)

# # --------------------------
# # LOAD FILES
# # --------------------------
# model = joblib.load("model.pkl")
# crop_encoder = joblib.load("crop_encoder.pkl")
# city_encoder = joblib.load("city_encoder.pkl")

# # --------------------------
# # TITLE
# # --------------------------
# st.title("🌾 AgriPrice AI")
# st.subheader("AI-Based Smart Crop Price Prediction & Market Intelligence")

# # --------------------------
# # SIDEBAR
# # --------------------------
# st.sidebar.header("Select Inputs")

# crop = st.sidebar.selectbox("Crop", crop_encoder.classes_)
# city = st.sidebar.selectbox("City", city_encoder.classes_)
# month = st.sidebar.slider("Month", 1, 12, 6)

# crop_val = crop_encoder.transform([crop])[0]
# city_val = city_encoder.transform([city])[0]

# # --------------------------
# # MAIN PREDICTION
# # --------------------------
# pred = model.predict([[month, crop_val, city_val]])[0]

# results = []

# for c in city_encoder.classes_:
#     c_val = city_encoder.transform([c])[0]
#     p = model.predict([[month, crop_val, c_val]])[0]
#     results.append([c, round(p,2)])

# df = pd.DataFrame(results, columns=["City","Predicted Price"])

# best_city = df.loc[df["Predicted Price"].idxmax(),"City"]
# best_price = df["Predicted Price"].max()

# # --------------------------
# # METRICS
# # --------------------------
# col1,col2,col3 = st.columns(3)

# with col1:
#     st.metric("📍 Selected City Price", f"Rs {pred:.2f}")

# with col2:
#     st.metric("🏆 Best City", best_city)

# with col3:
#     st.metric("💰 Highest Price", f"Rs {best_price:.2f}")

# # --------------------------
# # AI RECOMMENDATION
# # --------------------------
# st.success(
# f"🤖 AI Recommendation: Sell **{crop}** in **{best_city}** during month **{month}** for higher expected return."
# )

# # --------------------------
# # TABLE
# # --------------------------
# st.write("## 📊 Price Comparison Table")
# st.dataframe(df, use_container_width=True)

# # Download
# csv = df.to_csv(index=False).encode("utf-8")

# st.download_button(
#     "⬇ Download Comparison CSV",
#     csv,
#     "comparison_report.csv",
#     "text/csv"
# )

# # --------------------------
# # GRAPH 1 MULTI-LINE
# # --------------------------
# st.write("## 📈 Price Trend Across Cities")

# fig1, ax1 = plt.subplots(figsize=(12,6))

# colors = ["green","blue","red","orange","purple"]

# for i, c in enumerate(city_encoder.classes_):
#     c_val = city_encoder.transform([c])[0]
#     months = list(range(1,13))
#     prices = []

#     for m in months:
#         p = model.predict([[m, crop_val, c_val]])[0]
#         prices.append(p)

#     ax1.plot(months, prices, marker="o",
#              linewidth=2.5,
#              label=c,
#              color=colors[i])

# ax1.set_title(f"{crop} Price Trend")
# ax1.set_xlabel("Month")
# ax1.set_ylabel("Price")
# ax1.grid(True)
# ax1.legend()

# st.pyplot(fig1)

# # --------------------------
# # GRAPH 2 BAR
# # --------------------------
# st.write("## 🌍 Month-wise City Comparison")

# fig2, ax2 = plt.subplots(figsize=(12,6))

# bars = ax2.bar(df["City"], df["Predicted Price"], color=colors)

# for bar in bars:
#     y = bar.get_height()
#     ax2.text(bar.get_x()+bar.get_width()/2, y+10,
#              f"{y:.0f}", ha="center")

# ax2.set_title(f"{crop} Prices in Month {month}")
# ax2.set_xlabel("City")
# ax2.set_ylabel("Price")

# st.pyplot(fig2)

# # --------------------------
# # FOOTER
# # --------------------------
# st.write("---")
# st.caption("Machine Learning Model: Random Forest Regressor | Developed for AI Lab Mid Project")



import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="AgriPrice AI",
    page_icon="🌾",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM STYLE
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f8fff8;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD MODEL FILES
# ---------------------------------------------------
model = joblib.load("model.pkl")
crop_encoder = joblib.load("crop_encoder.pkl")
city_encoder = joblib.load("city_encoder.pkl")

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("🌾 AgriPrice AI")
st.subheader("AI-Based Smart Crop Price Prediction & Market Intelligence System")

st.write("---")

# ---------------------------------------------------
# SIDEBAR INPUTS
# ---------------------------------------------------
st.sidebar.header("Select Inputs")

crop = st.sidebar.selectbox(
    "Select Crop",
    crop_encoder.classes_
)

city = st.sidebar.selectbox(
    "Select City",
    city_encoder.classes_
)

month = st.sidebar.slider(
    "Select Month",
    1, 12, 6
)

# ---------------------------------------------------
# ENCODE INPUTS
# ---------------------------------------------------
crop_val = crop_encoder.transform([crop])[0]
city_val = city_encoder.transform([city])[0]

# ---------------------------------------------------
# MAIN PREDICTION
# ---------------------------------------------------
predicted_price = model.predict([[month, crop_val, city_val]])[0]

# ---------------------------------------------------
# ALL CITY COMPARISON
# ---------------------------------------------------
results = []

for c in city_encoder.classes_:
    c_val = city_encoder.transform([c])[0]
    p = model.predict([[month, crop_val, c_val]])[0]

    results.append({
        "City": c,
        "Predicted Price": round(p, 2)
    })

df = pd.DataFrame(results)

# Best city
best_row = df.loc[df["Predicted Price"].idxmax()]
best_city = best_row["City"]
best_price = best_row["Predicted Price"]

# ---------------------------------------------------
# TOP METRICS
# ---------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📍 Selected City Price", f"Rs {predicted_price:.2f}")

with col2:
    st.metric("🏆 Best City to Sell", best_city)

with col3:
    st.metric("💰 Highest Expected Price", f"Rs {best_price:.2f}")

# ---------------------------------------------------
# AI RECOMMENDATION
# ---------------------------------------------------
st.success(
    f"🤖 AI Recommendation: Sell {crop} in {best_city} during month {month} for better expected profit."
)

# ---------------------------------------------------
# TABLE
# ---------------------------------------------------
st.write("## 📊 Price Comparison Table")
st.dataframe(df, use_container_width=True)

# ---------------------------------------------------
# DOWNLOAD CSV
# ---------------------------------------------------
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Comparison Report",
    data=csv,
    file_name="comparison_report.csv",
    mime="text/csv"
)

# ---------------------------------------------------
# INTERACTIVE LINE GRAPH
# ---------------------------------------------------
st.write("## 📈 Interactive Price Trend Across Cities")

trend_data = []

for c in city_encoder.classes_:
    c_val = city_encoder.transform([c])[0]

    for m in range(1, 13):
        p = model.predict([[m, crop_val, c_val]])[0]

        trend_data.append({
            "Month": m,
            "Price": round(p, 2),
            "City": c
        })

trend_df = pd.DataFrame(trend_data)

fig1 = px.line(
    trend_df,
    x="Month",
    y="Price",
    color="City",
    markers=True,
    title=f"{crop} Price Trend Across Cities"
)

fig1.update_layout(
    hovermode="x unified",
    xaxis=dict(dtick=1)
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------------------
# INTERACTIVE BAR GRAPH
# ---------------------------------------------------
st.write("## 🌍 Current Month City Comparison")

fig2 = px.bar(
    df,
    x="City",
    y="Predicted Price",
    color="City",
    text="Predicted Price",
    title=f"{crop} Prices in Month {month}"
)

fig2.update_traces(texttemplate='%{text:.0f}', textposition='outside')

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.write("---")
st.caption("Machine Learning Model: Random Forest Regressor | Developed for AI Lab Mid Project")


