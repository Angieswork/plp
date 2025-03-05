# Import necessary libraries
import pandas as pd
# Import necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
# Import necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# Import necessary libraries
from sklearn.metrics import classification_report, confusion_matrix
# Import necessary libraries
from flask import Flask, request, jsonify
import pickle


# Sample data: Customer reviews
data = {
    'review': [
        'I love this product!',
        'This is the worst product I have ever bought.',
        'Great quality and fast delivery.',
        'Not worth the money.',
        'Highly recommend this product.'
    ],
    'sentiment': ['positive', 'negative', 'positive', 'negative', 'positive']
}

# Create a DataFrame
df = pd.DataFrame(data)
print(df)



# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Sample text preprocessing function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Apply preprocessing to the DataFrame
df['cleaned_review'] = df['review'].apply(preprocess_text)
print(df[['review', 'cleaned_review']])



# Convert text data to numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['cleaned_review'])
y = df['sentiment']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Select the logistic regression model
model = LogisticRegression()



# Train the model
model.fit(X_train, y_train)


# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))



# Save the model and vectorizer
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

# Create a Flask app
app = Flask(__name__)

# Load the model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['review']
    cleaned_review = preprocess_text(data)
    X = vectorizer.transform([cleaned_review])
    prediction = model.predict(X)
    return jsonify({'sentiment': prediction[0]})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
