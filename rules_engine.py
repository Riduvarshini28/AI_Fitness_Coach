def get_recommendations(user_data):
    BMI = user_data.get("BMI")
    goal = user_data.get("Fitness_Goal")
    gender = user_data.get("Gender")
    sleep = user_data.get("Sleep_Hours")
    rhr = user_data.get("Resting_Heart_Rate")
    previous_injury = user_data.get("Previous_Injury")
    daily_steps = user_data.get("Daily_Steps")
    workout_pref = user_data.get("Workout_Preference")
    workout_time = user_data.get("Workout_Time")

    rec = {
        "BMI": BMI,
        "Recommendations": [],
        "Workout_Plan": [],
        "Improvements": [],
        "Motivation": ""
    }

    # --- BMI Insights ---
    if BMI < 18.5:
        rec["Recommendations"].append("Underweight — increase calorie intake and strength training.")
    elif 18.5 <= BMI <= 24.9:
        rec["Recommendations"].append("Healthy BMI — maintain balance between cardio and weights.")
    elif BMI < 30:
        rec["Recommendations"].append("Overweight — focus on cardio, steps, and light resistance workouts.")
    else:
        rec["Recommendations"].append("Obese — adopt calorie deficit + low-impact exercises like swimming.")

    # --- Workout Time Normalization ---
    t = max(30, workout_time)

    # --- Personalized Weekly Plan ---
    if goal == "Weight Loss":
        rec["Workout_Plan"] = [
            f"Day 1 – 20 min brisk walk + 15 min HIIT + 10 min stretching",
            f"Day 2 – {t} min cycling or skipping",
            "Day 3 – 30 min jog + 15 min abs workout (plank, crunches)",
            "Day 4 – Active rest (yoga, mobility)",
            "Day 5 – 40 min running or stair climb",
            "Day 6 – 30 min strength circuit + 10 min cardio",
            "Day 7 – Rest or light yoga"
        ]
    elif goal == "Muscle Gain":
        rec["Workout_Plan"] = [
            "Day 1 – Chest + Triceps (bench press, pushups)",
            "Day 2 – Back + Biceps (rows, curls)",
            "Day 3 – Legs (squats, lunges)",
            "Day 4 – Shoulders + Abs (plank, raises)",
            "Day 5 – Full body (compound lifts)",
            "Day 6 – Rest or walk 30 min",
            "Day 7 – Stretch & recovery"
        ]
    elif goal == "Endurance":
        rec["Workout_Plan"] = [
            "Day 1 – 45 min steady-state run",
            "Day 2 – 60 min cycling/swimming",
            "Day 3 – Interval sprints (6 × 2 min)",
            "Day 4 – Strength + stability training",
            "Day 5 – Long run (60+ min)",
            "Day 6 – Core & yoga",
            "Day 7 – Rest"
        ]
    else:
        rec["Workout_Plan"] = [
            "Day 1 – 30 min walk + 15 min bodyweight circuit",
            "Day 2 – 30 min cardio",
            "Day 3 – 30 min strength (pushups, squats)",
            "Day 4 – Stretching + mobility",
            "Day 5 – 30 min yoga / cycling",
            "Day 6 – Core + balance drills",
            "Day 7 – Rest"
        ]

    # --- Modify for Injury ---
    if previous_injury != "None":
        if "Knee" in previous_injury:
            rec["Workout_Plan"] = [f"{w} (avoid running/jumping; prefer cycling or swimming)" for w in rec["Workout_Plan"]]
        elif "Back" in previous_injury:
            rec["Workout_Plan"] = [f"{w} (avoid heavy lifts; focus on core)" for w in rec["Workout_Plan"]]
        elif "Shoulder" in previous_injury:
            rec["Workout_Plan"] = [f"{w} (avoid overhead exercises)" for w in rec["Workout_Plan"]]

    # --- Improvements ---
    if sleep < 7:
        rec["Improvements"].append("Increase sleep to 7–8 hrs for recovery.")
    if daily_steps < 8000:
        rec["Improvements"].append("Target 10,000 steps/day for better metabolism.")
    if rhr > 85:
        rec["Improvements"].append("Include breathing or light cardio to reduce heart rate.")
    if workout_time < 30:
        rec["Improvements"].append("Try minimum 30–40 min sessions for visible progress.")

    rec["Motivation"] = "Consistency > Intensity. Keep showing up, and results will follow! 💪"

    return rec
