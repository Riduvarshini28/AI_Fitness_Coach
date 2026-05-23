# analyze_data.py
import matplotlib
matplotlib.use('Agg')  # Prevent GUI-related issues in Flask
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def generate_calorie_chart(predicted_calories):
    """Generate a polished, aesthetic bar chart comparing predicted vs goal calories."""
    try:
        goal_value = 2000  # Example daily target calories
        values = [goal_value, predicted_calories]
        labels = ['Recommended (Goal)', 'Predicted (You)']

        # Chart setup
        plt.figure(figsize=(5.5, 4))
        bars = plt.bar(
            labels,
            values,
            color=['#cce5ff', '#0078d7'],  # soft blue + dark blue theme
            width=0.55,
            edgecolor='#005fa3'
        )

        # Add data labels on top of bars
        for bar in bars:
            yval = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                yval + 30,
                f'{yval:.0f}',
                ha='center',
                va='bottom',
                fontsize=10,
                fontweight='600',
                color='#333'
            )

        # Titles and styling
        plt.title("Calories Comparison", fontsize=14, fontweight='bold', color='#023047', pad=15)
        plt.ylabel("Calories", fontsize=11, labelpad=10)
        plt.grid(axis='y', linestyle='--', alpha=0.3)
        plt.tight_layout()
        plt.gca().set_facecolor("#f8faff")
        plt.box(False)

        # Convert to base64 image
        buffer = BytesIO()
        plt.savefig(buffer, format="png", bbox_inches="tight", dpi=130)
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()
        return image_base64

    except Exception as e:
        print("⚠️ Chart generation error:", e)
        return None
