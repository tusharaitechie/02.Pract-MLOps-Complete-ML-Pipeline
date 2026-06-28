# 🚀 MLOps Complete ML Pipeline using DVC

A complete end-to-end Machine Learning Pipeline built using **Python**, **Scikit-learn**, **Git**, and **DVC (Data Version Control)**.

This project demonstrates how to build a reproducible Machine Learning workflow by separating the entire pipeline into independent stages such as Data Ingestion, Data Preprocessing, Feature Engineering, Model Building, and Model Evaluation.

---

# 📌 Project Objectives

- Build a modular Machine Learning pipeline
- Version datasets using DVC
- Automate pipeline execution
- Track model metrics
- Learn MLOps best practices
- Create a reproducible workflow

---

# 🛠️ Tech Stack

- Python 3.11
- Pandas
- NumPy
- Scikit-learn
- NLTK
- WordCloud
- YAML
- Git
- DVC

---

# 📁 Project Structure

```
02.Pract-MLOps-Complete-ML-Pipeline
│
├── data
│   ├── raw
│   ├── interim
│   └── processed
│
├── models
│   └── model.pkl
│
├── reports
│   └── metrics.json
│
├── logs
│
├── src
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_building.py
│   └── model_evaluation.py
│
├── dvc.yaml
├── dvc.lock
├── params.yaml
├── requirements.txt
└── README.md
```

---

# 🔄 Pipeline Workflow

```
Data Ingestion
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Model Building
      │
      ▼
Model Evaluation
      │
      ▼
Metrics Generation
```

---

# ⚙️ Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/tusharaitechie/02.Pract-MLOps-Complete-ML-Pipeline.git

cd 02.Pract-MLOps-Complete-ML-Pipeline
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv ml_env
ml_env\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv ml_env
source ml_env/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not available:

```bash
pip install pandas numpy matplotlib scikit-learn nltk wordcloud xgboost dvc pyyaml
```

---

# 🚀 Running the Project

Run the complete pipeline:

```bash
dvc repro
```

This command automatically executes:

- Data Ingestion
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation

Only the modified stages are executed.

---

# 📊 Evaluation Metrics

After successful execution, evaluation metrics are saved in:

```
reports/metrics.json
```

Example:

```json
{
    "accuracy": 0.97,
    "precision": 1.00,
    "recall": 0.79,
    "auc": 0.98
}
```

---

# 📈 DVC Commands Reference

## Initialize DVC

```bash
dvc init
```

---

## Run Complete Pipeline

```bash
dvc repro
```

---

## Check Pipeline Status

```bash
dvc status
```

---

## Visualize Pipeline

```bash
dvc dag
```

---

## Show Metrics

```bash
dvc metrics show
```

---

## Compare Metrics

```bash
dvc metrics diff
```

---

## Add Dataset

```bash
dvc add data
```

---

## Add Model

```bash
dvc add models
```

---

## Push Data to Remote Storage

```bash
dvc push
```

---

## Pull Data from Remote Storage

```bash
dvc pull
```

---

## Fetch Data

```bash
dvc fetch
```

---

## Checkout Tracked Files

```bash
dvc checkout
```

---

## Show Pipeline Graph

```bash
dvc dag
```

---

# 📌 Git Commands Used

Clone Repository

```bash
git clone <repository-url>
```

Check Status

```bash
git status
```

Stage Files

```bash
git add .
```

Commit Changes

```bash
git commit -m "Your Commit Message"
```

Push Changes

```bash
git push origin main
```

Pull Latest Changes

```bash
git pull origin main
```

---

# 📂 Important Configuration Files

## dvc.yaml

Contains complete pipeline stages.

Example stages:

- Data Ingestion
- Data Preprocessing
- Feature Engineering
- Model Building
- Model Evaluation

---

## params.yaml

Contains configurable parameters such as:

- Test Size
- Maximum Features
- Random State
- Number of Estimators
- Model Paths
- Dataset Paths

---

# 🧠 Why DVC?

DVC helps in:

- Version controlling datasets
- Tracking ML pipelines
- Reproducibility
- Experiment management
- Efficient collaboration
- Data lineage

Unlike Git, DVC is designed specifically for large datasets and Machine Learning artifacts.

---

# 📌 Best Practices Followed

- Modular code structure
- Logging implemented
- Configuration through YAML
- Separate pipeline stages
- Version controlled data
- Reproducible experiments
- Metrics tracking
- Clean project architecture

---

# 🚨 Common Issues

## ModuleNotFoundError

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## DVC Pipeline Error

Re-run pipeline:

```bash
dvc repro
```

---

## Check Pipeline Status

```bash
dvc status
```

---

## View Pipeline Graph

```bash
dvc dag
```

---

# 📚 Learning Outcomes

By completing this project, you will understand:

- Machine Learning Pipeline
- Data Version Control
- Reproducible ML
- YAML Configuration
- Model Evaluation
- Feature Engineering
- Git + DVC Workflow
- MLOps Fundamentals

---

# 📖 References

- https://dvc.org/doc
- https://scikit-learn.org/
- https://pandas.pydata.org/
- https://numpy.org/
- https://docs.python.org/3/

---

# 👨‍💻 Author

**Tushar Aitechie**

GitHub:
https://github.com/tusharaitechie

---

# ⭐ If you found this project useful, don't forget to Star the repository!