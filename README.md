# 🔐 Phishing URL Detector

A machine learning-based system to classify URLs as **phishing** or **legitimate** using feature engineering and classical ML models.

Built as a portfolio project to demonstrate practical ML skills including data collection, feature engineering, model training, and evaluation.

---

## 🚀 Project Status

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 0 | Environment Setup | ✅ Complete |
| Phase 1 | Dataset Collection & Cleaning | ✅ Complete |
| Phase 2 | Feature Extraction | 🔄 In Progress |
| Phase 3 | Model Training | ⏳ Pending |
| Phase 4 | Evaluation & Visualization | ⏳ Pending |
| Phase 5 | Flask Web App (Demo) | ⏳ Pending |

---

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **ML Libraries:** scikit-learn, XGBoost
- **Data:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **URL Parsing:** tldextract
- **Web App (bonus):** Flask

---

## 📁 Project Structure
phishing-url-detector/

├── data/

│   ├── raw/                # Original downloaded dataset

│   └── processed/          # Feature-extracted CSV (model-ready)

├── notebooks/              # Jupyter notebooks (EDA, experiments)

├── src/                    # Clean Python scripts

│   ├── feature_extraction.py

│   ├── train_model.py

│   └── predict.py

├── models/                 # Saved trained model (.pkl files)

├── app/                    # Flask demo web app

├── requirements.txt        # All dependencies

└── README.md
---

## 📊 Dataset

- **Source:** Kaggle — Phishing Site URLs Dataset
- **Classes:** Phishing (1) vs Legitimate (0)
- **Preprocessing:** Removed duplicates, handled missing values, standardized labels

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/manahil-habib31/phishing-url-detector.git
cd phishing-url-detector
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Jupyter Notebook
```bash
jupyter notebook
```

---

## 🔍 Features Being Extracted (Phase 2)

| Feature | Description |
|---------|-------------|
| URL Length | Longer URLs often indicate phishing |
| Has @ Symbol | Used to trick browsers |
| Has IP Address | Legitimate sites rarely use raw IPs |
| Number of Subdomains | Excess subdomains = suspicious |
| HTTPS Present | Basic security check |
| Suspicious Keywords | "verify", "login", "secure", "confirm" |
| Number of Hyphens | Common in fake domain names |
| URL Shortener Used | Hides real destination |
| Path Depth | Very deep paths are suspicious |
| Number of Digits | Random digits = generated URLs |

---

## 📈 Models (Phase 3)

Three models will be trained and compared:
- Logistic Regression (baseline)
- Random Forest
- XGBoost

Evaluation metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC

---

## 👩‍💻 Author

**Manahil Habib**
Pre-final year Software Engineering Student
Fatima Jinnah Women University, Rawalpindi

---

## 📌 Note

This project is actively under development.
Dataset CSV files are excluded from version control (see `.gitignore`).