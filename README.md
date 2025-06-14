# MLflow Docker Project: Iris Classification

This is a clean, portfolio-ready machine learning project using:
- **scikit-learn** to train a Random Forest model on the Iris dataset
- **MLflow** to track metrics, parameters, and the trained model
- **Docker** for reproducible container-based execution

## 🔍 What It Does
- Loads and preprocesses the classic Iris dataset
- Splits it into training/testing sets
- Trains a `RandomForestClassifier`
- Logs model, metrics, and an input schema using MLflow

## 🐳 How to Run with Docker

```bash
docker build -t mlflow-docker .
docker run mlflow-docker
```

## 📦 What's Included
- `main.py`: Your full training and MLflow logging script
- `Dockerfile`: Container setup
- `requirements.txt`: All dependencies
- `README.md`: Project documentation

## 🧠 Why It Matters
This project demonstrates how to:
- Train an ML model
- Track and reproduce experiments with MLflow
- Package everything in Docker for portability and deployment

Ideal for showcasing in technical interviews or portfolios.
