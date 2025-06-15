# 🧪 MLflow Docker Iris Project

Train, track, and version a machine learning model using `scikit-learn`, `MLflow`, and `Docker` — all on the classic Iris dataset.

This project demonstrates an end-to-end ML workflow:
- Preprocessing with pandas
- Modeling with RandomForest
- Experiment tracking with MLflow
- Reproducibility via Docker

---

## 🚀 Quick Start

### 🔧 Run with Docker

docker build -t mlflow-docker .
docker run -p 5000:5000 mlflow-docker

### 🐍 Or run locally

pip install -r requirements.txt
python main.py

---

## 📂 Project Structure
```
mlflow_docker_project/
├── main.py           # Trains and logs a model with MLflow
├── requirements.txt  # Python dependencies
├── Dockerfile        # Reproducible environment
├── README.md         # Project overview
└── mlruns/           # MLflow experiment tracking (auto-generated)
```

---

## 📊 What It Does

- Loads and preprocesses the Iris dataset
- Trains a RandomForestClassifier
- Logs parameters, metrics, and the model itself to MLflow
- Supports input signature + example for reproducible deployment
- Containerized using Docker for cross-platform repeatability

---

## 🔍 Sample Output

Logged model with accuracy: 1.0

MLflow run is stored in `mlruns/` and viewable via:

```
mlflow ui
```

 ---

## 🧠 Why This Project?

This project is designed to showcase:

- Practical use of MLflow for MLOps and experiment tracking
- How to train and deploy an ML model in a reproducible container
- Real-world tools used by companies like Canonical, DataRobot, and Hugging Face

---

## 🛠️ Tools Used

- Python 3
- Pandas / Scikit-learn
- MLflow
- Docker

---

## 📚 Inspired By

This project was built and customized as a professional portfolio piece to demonstrate machine learning workflow best practices with tools used in modern MLOps pipelines.

---

## 👤 Author

Matthew Burns  
📫 [LinkedIn](https://www.linkedin.com/in/mattburns23) • [GitHub](https://github.com/MattBurns23)

---

## 📝 License

MIT — feel free to fork and build upon it.
