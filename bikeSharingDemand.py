import argparse
import os

from utils.io_utils import load_data


parser = argparse.ArgumentParser(description="passing in test flag to run predictions")
parser.add_argument("--test", action="store_true", help="Load and run predictions on test.csv instead of training data")
args = parser.parse_args()

output_dir = "./outputs"
model_path = os.path.join(output_dir, "model.pkl")

# --------------------------------
#  Load Data
# --------------------------------
df = load_data(args.test)