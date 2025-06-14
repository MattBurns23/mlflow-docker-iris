import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from mlflow.models.signature import infer_signature
import pandas as pd

# Load and prepare data
iris = load_iris()
df_X = pd.DataFrame(iris.data, columns=iris.feature_names).astype('float64')
df_y = pd.Series(iris.target).astype('float64')  # cast labels to float

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df_X, df_y, test_size=0.2, random_state=42
)

# Train model
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

# Prepare MLflow logging
input_example = X_test[:1]
signature = infer_signature(X_test, clf.predict(X_test))

# Log model with clean schema
with mlflow.start_run():
    mlflow.sklearn.log_model(
        sk_model=clf,
        name="model",
        input_example=input_example,
        signature=signature
    )
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_param("n_estimators", 100)

print(f"Logged model with accuracy: {accuracy}")
