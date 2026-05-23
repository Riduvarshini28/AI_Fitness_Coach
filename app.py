from flask import Flask, render_template, request
import joblib
import numpy as np
from rules_engine import get_recommendations
from knowledge_base import get_nutrition_plan
import os

app = Flask(__name__)

model_path = r"C:\Users\Riduvarshini A T\Documents\AI_Fitness_Coach\data\merged_csvs\calorie_predictor.pkl"

if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    raise FileNotFoundError("❌ Model not found!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        gender = request.form['gender']
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        food_pref = request.form['food_pref']
        daily_steps = int(request.form['daily_steps'])
        rhr = int(request.form['resting_hr'])
        sleep_hours = float(request.form['sleep_hours'])
        previous_injury = request.form['previous_injury']
        goal = request.form['fitness_goal']
        workout_pref = request.form['workout_preference']
        workout_time = int(request.form['workout_time'])
        hormonal_status = request.form.get('hormonal_status', 'Normal')

        bmi = round(weight / ((height / 100) ** 2), 2)
        if bmi < 18.5:
            bmi_category = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            bmi_category = "Normal Weight"
        elif 25 <= bmi <= 29.9:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obese"

        total_steps = daily_steps
        very_active = min(max(int((workout_time / 60) * 60), 0), 100)
        fairly_active = 30 if goal == "Endurance" else 15
        lightly_active = int((sleep_hours * 10) / 2)
        sedentary = int((24 - sleep_hours) * 40)

        input_data = np.array([[total_steps, very_active, fairly_active, lightly_active, sedentary]])

        predicted_calories = round(model.predict(input_data)[0], 2)
        target_calories = round(predicted_calories + 200 if goal == "Muscle Gain" else predicted_calories - 200, 2)

        nutrition_data = get_nutrition_plan(food_pref, goal, gender, hormonal_status)
        user_data = {
            "BMI": bmi, "Fitness_Goal": goal, "Gender": gender,
            "Sleep_Hours": sleep_hours, "Resting_Heart_Rate": rhr,
            "Previous_Injury": previous_injury, "Daily_Steps": daily_steps,
            "Workout_Preference": workout_pref, "Workout_Time": workout_time
        }
        recommendations = get_recommendations(user_data)
        chart_data = {"predicted": predicted_calories, "target": target_calories}

        return render_template('index.html',
                               predicted_calories=predicted_calories,
                               target_calories=target_calories,
                               recommendations=recommendations,
                               nutrition_data=nutrition_data,
                               bmi=bmi,
                               bmi_category=bmi_category,
                               chart_data=chart_data)
    except Exception as e:
        return render_template('index.html', error=f"⚠️ Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
