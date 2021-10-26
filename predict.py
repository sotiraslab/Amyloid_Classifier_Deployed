import argparse
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import load
from standardizer import *

feature_subset_dict = {
    "0": "MRI, demographic, BMI, genetic, and cognitive biomarkers",
    "1": "demographic, BMI, genetic, and cognitive biomarkers",
    "2": "demographic, BMI, and genetic biomarkers",
    "3": "demographic, BMI, and cognitive biomarkers",
    "p": "demographic, BMI, genetic, cognitive, and plasma biomarkers",
}

# initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input path (.csv)", type=str)
parser.add_argument("-o", "--output", help="output path (.csv)", type=str)
parser.add_argument("-f", "--feature", help="feature subset: {0, 1, 2, 3, p}", type=str)
parser.add_argument(
    "-m", "--memory", help="logical delayed recall memory test", type=str
)
args = parser.parse_args()

# parse arguments
input_path = args.input
output_path = args.output
feature_subset = args.feature
memory_test = args.memory

# log parsed arguments
print(f"input: {input_path}")
print(f"output: {output_path}")
print(f"feature subset (0, 1, 2, 3, or p): {feature_subset_dict[feature_subset]}")
print(f"logical delayed recall memory test (r or 3): {memory_test}")

# load input dataframe
input_df = pd.read_csv(input_path)
# create output dataframe
output_df = input_df.copy(deep=True)
# model directory
model_dir = f"models/feature_subset_{feature_subset}"

# z-score delayed memory recall score
if feature_subset != "2":
    if memory_test == "r":
        input_df["LDELTOTAL"] = (input_df["LDELTOTAL"] - mem_mean) / mem_std
    elif memory_test == "3":
        input_df["LDELTOTAL"] = (input_df["LDELTOTAL"] - mem3_mean) / mem3_std
    elif memory_test == None:
        raise ValueError("Did not specify which logical memory test to use")
    else:
        raise ValueError(f"{memory_test} is not a valid option for logical memory test")

# iteratre for each model
for i in range(1, 6):
    # load model
    model = load(os.path.join(model_dir, f"model_{i}.joblib"))
    # make predictions
    output_df[f"prob_{i}"] = model.predict_proba(input_df.to_numpy())[:, 1]

# average prediction probabilties
prob_columns = [f"prob_{i}" for i in range(1, 6)]
output_df["prob"] = output_df[prob_columns].mean()

# save output
output_df.to_csv(output_path, index=False)
