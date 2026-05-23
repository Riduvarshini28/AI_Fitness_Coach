import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

data_path = r"C:\Users\Riduvarshini A T\Documents\AI_Fitness_Coach\data\merged_csvs"
activity_csv = os.path.join(data_path, "dailyActivity_merged.csv")
out_model = os.path.join(data_path, "calorie_predictor.pkl")

df = pd.read_csv(activity_csv)

# Select model features (Fitbit data columns)
features = ["TotalSteps", "VeryActiveMinutes", "FairlyActiveMinutes", "LightlyActiveMinutes", "SedentaryMinutes"]
target = "Calories"

# Handle missing columns or data
for col in features:
    if col not in df.columns:
        df[col] = 0
df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# Split, train, evaluate
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"✅ Trained model — MAE: {mae:.2f}, R²: {r2:.2f}")

# Save the trained model
joblib.dump(model, out_model)
print("💾 Saved model to:", out_model)
