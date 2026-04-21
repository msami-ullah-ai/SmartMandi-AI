import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# Load dataset
df = pd.read_csv("prices.csv")

print("Dataset Loaded Successfully")
print(df.head())

# Encode categorical columns
crop_encoder = LabelEncoder()
city_encoder = LabelEncoder()

df["Crop"] = crop_encoder.fit_transform(df["Crop"])
df["City"] = city_encoder.fit_transform(df["City"])

# Features and Target
X = df[["Month", "Crop", "City"]]
y = df["Price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Train Model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
pred = model.predict(X_test)

# Accuracy Metrics
r2 = r2_score(y_test, pred)
mae = mean_absolute_error(y_test, pred)

print("\nModel Performance")
print("R2 Score:", round(r2, 3))
print("MAE:", round(mae, 2))

# Save Files
joblib.dump(model, "model.pkl")
joblib.dump(crop_encoder, "crop_encoder.pkl")
joblib.dump(city_encoder, "city_encoder.pkl")

print("\nFiles Saved Successfully!")
print("model.pkl")
print("crop_encoder.pkl")
print("city_encoder.pkl")
