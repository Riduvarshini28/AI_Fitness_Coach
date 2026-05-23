def get_nutrition_plan(food_pref, goal, gender, hormonal_status):
    plan = {
        "Macronutrient_Guidelines": [],
        "Macro_Food_Plan": [],
        "Hormonal_Support": [],
        "Sample_Meal_Plan": []
    }

    # --- Macronutrient Guidelines based on Goal ---
    if goal == "Weight Loss":
        plan["Macronutrient_Guidelines"].append("Calorie Deficit: 40% Protein, 30% Carbs, 30% Fats")
    elif goal == "Muscle Gain":
        plan["Macronutrient_Guidelines"].append("Calorie Surplus: 40% Carbs, 35% Protein, 25% Fats")
    elif goal == "Endurance":
        plan["Macronutrient_Guidelines"].append("High Energy: 55% Carbs, 25% Protein, 20% Fats")
    else:
        plan["Macronutrient_Guidelines"].append("Balanced Diet: 40% Carbs, 30% Protein, 30% Fats")

    # --- Food Suggestions based on Preference ---
    if food_pref == "Vegetarian":
        plan["Macro_Food_Plan"] = [
            "Protein: Paneer, tofu, lentils, chickpeas, soybeans",
            "Carbs: Oats, brown rice, quinoa, sweet potatoes",
            "Fats: Nuts, seeds, olive oil, avocado"
        ]
    elif food_pref == "Non-Vegetarian":
        plan["Macro_Food_Plan"] = [
            "Protein: Chicken breast, eggs, fish, lean meat",
            "Carbs: Brown rice, oats, potatoes, fruits",
            "Fats: Olive oil, almonds, walnuts, flaxseeds"
        ]
    else:  # Vegan
        plan["Macro_Food_Plan"] = [
            "Protein: Tofu, tempeh, lentils, beans",
            "Carbs: Quinoa, oats, fruits, sweet potatoes",
            "Fats: Avocado, coconut, chia seeds, sunflower seeds"
        ]

    # --- Hormonal Support (for Females only) ---
    if gender == "Female":
        if hormonal_status == "PCOS":
            plan["Hormonal_Support"] = [
                "Include flaxseeds, turmeric, and green tea (anti-inflammatory).",
                "Reduce dairy, refined carbs, and high-sugar foods.",
                "Opt for low-GI foods like oats, lentils, leafy greens, and nuts."
            ]
        elif hormonal_status == "PCOD":
            plan["Hormonal_Support"] = [
                "Focus on magnesium & omega-3–rich foods (spinach, almonds, fish).",
                "Avoid processed foods, sugar, and white flour.",
                "Include B-vitamin & zinc-rich foods like pumpkin seeds, chickpeas."
            ]
        else:
            plan["Hormonal_Support"] = [
                "Maintain balanced macros for menstrual cycle regularity.",
                "Stay hydrated, include iron-rich foods (beetroot, spinach).",
                "Sleep 7–8 hours to support hormonal balance."
            ]

    # --- 1-Day Sample Meal Plan ---
    if goal == "Weight Loss":
        plan["Sample_Meal_Plan"] = [
            "🥣 Breakfast: Oats with fruits + green tea",
            "🥗 Lunch: Brown rice + paneer/tofu curry + salad",
            "🍎 Snack: Handful of nuts or fruit",
            "🍛 Dinner: Vegetable soup + lentils or grilled chicken"
        ]
    elif goal == "Muscle Gain":
        plan["Sample_Meal_Plan"] = [
            "🍳 Breakfast: 4 egg whites / tofu + oats + milk",
            "🥗 Lunch: Chicken breast or dal + rice + veggies",
            "🥤 Snack: Peanut butter toast + banana shake",
            "🍝 Dinner: Whole wheat pasta + paneer or fish + olive oil drizzle"
        ]
    elif goal == "Endurance":
        plan["Sample_Meal_Plan"] = [
            "🥣 Breakfast: Oats + honey + nuts + banana",
            "🥗 Lunch: Quinoa + lentils + green veggies",
            "🍞 Snack: Greek yogurt + fruits or smoothie",
            "🍛 Dinner: Sweet potato + beans + salad"
        ]
    else:
        plan["Sample_Meal_Plan"] = [
            "🍳 Breakfast: Poha / Eggs / Fruit bowl",
            "🥗 Lunch: Balanced plate with carbs + protein + veggies",
            "🍎 Snack: Dry fruits / Smoothie",
            "🍛 Dinner: Light khichdi / Soup / Grilled paneer"
        ]

    return plan
