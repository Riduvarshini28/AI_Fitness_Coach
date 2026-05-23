import os
import pandas as pd

# Base data path
base_path = r"C:\Users\Riduvarshini A T\Documents\AI_Fitness_Coach\data"
output_folder = os.path.join(base_path, "merged_csvs")
os.makedirs(output_folder, exist_ok=True)

# Function to merge CSVs from both folders
def merge_csvs():
    csv_dict = {}

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".csv"):
                name = file.lower()
                path = os.path.join(root, file)

                if name not in csv_dict:
                    csv_dict[name] = []
                csv_dict[name].append(path)

    for name, paths in csv_dict.items():
        dfs = [pd.read_csv(p) for p in paths]
        merged = pd.concat(dfs, ignore_index=True)
        out_path = os.path.join(output_folder, name)
        merged.to_csv(out_path, index=False)
        print(f"✅ Merged and saved: {out_path}")

merge_csvs()
print("🎉 All datasets merged successfully!")
