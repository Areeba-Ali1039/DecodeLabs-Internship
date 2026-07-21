"""
Project 2: Data Classification Using AI
Building a basic classification model using a small dataset (Iris).
Pipeline: Load -> Scale -> Split -> Train (KNN) -> Predict -> Evaluate
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, f1_score, accuracy_score

# ----  Load and understand the dataset ----
iris = load_iris()
X = iris.data         
y = iris.target       

print("Dataset shape:", X.shape)
print("Classes:", iris.target_names)
print("Feature names:", iris.feature_names)
print("-" * 50)

# ---- Scale the features (Gatekeeper Rule) ----
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---- Split data into training and testing sets ----
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
print("-" * 50)

# ---- Apply a simple classification algorithm (KNN) ----
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)   

# ---- Make predictions on unseen test data ----
predictions = model.predict(X_test)

# ---- Evaluate the model properly ----
accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average='weighted')

print("Accuracy:", round(accuracy * 100, 2), "%")
print("F1 Score (weighted):", round(f1, 3))
print("-" * 50)

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("-" * 50)

print("Classification Report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))

# ---- Bonus: Predict a brand-new, unseen flower sample ----
new_flower = [[5.1, 3.5, 1.4, 0.2]]  # example 
new_flower_scaled = scaler.transform(new_flower)
new_prediction = model.predict(new_flower_scaled)
print("Prediction for new flower sample:", iris.target_names[new_prediction[0]])
