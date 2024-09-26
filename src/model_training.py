from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

# Load the cleaned data
df = pd.read_csv('data/titanic_cleaned.csv')

# Split the dataset
X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)
