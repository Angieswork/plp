import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Step 1: Simulate medical image data (e.g., pixel values)
# Generate random data for 100 images, each with 256 features (pixel values)
X = np.random.rand(100, 256)  # Features: 100 images, 256 pixels each
y = np.random.randint(0, 2, 100)  # Labels: 0 (healthy) or 1 (tumor)

# Step 2: Train a Random Forest Classifier on the simulated data
model = RandomForestClassifier(n_estimators=100, random_state=42)  # Using 100 trees for better accuracy
model.fit(X, y)  # Fit the model to the training data

# Step 3: Simulate a new medical image for prediction
new_image = np.random.rand(1, 256)  # A new image with 256 pixel features

# Step 4: Predict if the new image contains a tumor
prediction = model.predict(new_image)

# Step 5: Print the result based on the prediction
print("Tumor detected!" if prediction[0] == 1 else "No tumor detected.")
