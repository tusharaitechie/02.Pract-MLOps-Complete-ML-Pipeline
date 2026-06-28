import os
import numpy as np
import pandas as pd
import pickle
import json
import logging

from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score

# -------------------------
# Logging Setup
# -------------------------
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("model_evaluation")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler = logging.FileHandler(os.path.join(log_dir, "model_evaluation.log"))
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


# -------------------------
# Load Model
# -------------------------
def load_model(model_path: str):
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        logger.debug(f"Model loaded from {model_path}")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise


# -------------------------
# Load Data
# -------------------------
def load_data(data_path: str):
    try:
        df = pd.read_csv(data_path)
        logger.debug(f"Data loaded from {data_path}")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise


# -------------------------
# Evaluate Model
# -------------------------
def evaluate_model(model, X_test, y_test):
    try:
        y_pred = model.predict(X_test)

        # probability check (safe for models without predict_proba)
        if hasattr(model, "predict_proba"):
            y_pred_proba = model.predict_proba(X_test)[:, 1]
            auc = roc_auc_score(y_test, y_pred_proba)
        else:
            auc = None

        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "auc": auc
        }

        logger.debug("Model evaluation completed")
        return metrics

    except Exception as e:
        logger.error(f"Error during evaluation: {e}")
        raise


# -------------------------
# Save Metrics
# -------------------------
def save_metrics(metrics: dict, output_path: str):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(metrics, f, indent=4)

        logger.debug(f"Metrics saved at {output_path}")

    except Exception as e:
        logger.error(f"Error saving metrics: {e}")
        raise


# -------------------------
# Main Function
# -------------------------
def main():
    try:
        model_path = "./models/model.pkl"
        data_path = "./data/processed/test_tfidf.csv"
        report_path = "./reports/metrics.json"

        model = load_model(model_path)
        data = load_data(data_path)

        X_test = data.iloc[:, :-1].values
        y_test = data.iloc[:, -1].values

        metrics = evaluate_model(model, X_test, y_test)

        save_metrics(metrics, report_path)

        print("\n✅ Model Evaluation Completed Successfully")
        print("📊 Metrics:")
        for k, v in metrics.items():
            print(f"{k}: {v}")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        print(f"Error: {e}")


# -------------------------
# Entry Point
# -------------------------
if __name__ == "__main__":
    main()