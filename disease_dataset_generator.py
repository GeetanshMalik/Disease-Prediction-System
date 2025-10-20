import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# symptom-disease dataset
symptoms_list = [
    'fever', 'cough', 'fatigue', 'difficulty_breathing', 'sore_throat',
    'runny_nose', 'headache', 'body_ache', 'chills', 'nausea',
    'vomiting', 'diarrhea', 'loss_of_taste', 'loss_of_smell', 'chest_pain',
    'rapid_heartbeat', 'dizziness', 'sweating', 'abdominal_pain', 'bloating',
    'constipation', 'joint_pain', 'muscle_weakness', 'rash', 'itching',
    'sneezing', 'watery_eyes', 'wheezing', 'shortness_of_breath', 'back_pain',
    'frequent_urination', 'burning_urination', 'blood_in_urine', 'weight_loss',
    'increased_thirst', 'blurred_vision', 'slow_healing', 'anxiety',
    'depression', 'insomnia', 'loss_of_appetite', 'weight_gain',
    'swollen_lymph_nodes', 'night_sweats', 'persistent_cough'
]

# Disease patterns with associated symptoms
disease_patterns = {
    'Common Cold': {
        'symptoms': ['runny_nose', 'sneezing', 'sore_throat', 'cough', 'mild_fever', 'headache', 'body_ache'],
        'probability': 0.85
    },
    'Influenza (Flu)': {
        'symptoms': ['fever', 'cough', 'sore_throat', 'body_ache', 'headache', 'fatigue', 'chills'],
        'probability': 0.88
    },
    'COVID-19': {
        'symptoms': ['fever', 'cough', 'fatigue', 'loss_of_taste', 'loss_of_smell', 'difficulty_breathing', 'body_ache'],
        'probability': 0.82
    },
    'Allergic Rhinitis': {
        'symptoms': ['sneezing', 'runny_nose', 'watery_eyes', 'itching', 'nasal_congestion'],
        'probability': 0.90
    },
    'Asthma': {
        'symptoms': ['wheezing', 'shortness_of_breath', 'chest_pain', 'cough', 'difficulty_breathing'],
        'probability': 0.87
    },
    'Bronchitis': {
        'symptoms': ['persistent_cough', 'chest_pain', 'fatigue', 'shortness_of_breath', 'mild_fever'],
        'probability': 0.83
    },
    'Gastroenteritis': {
        'symptoms': ['diarrhea', 'nausea', 'vomiting', 'abdominal_pain', 'fever', 'loss_of_appetite'],
        'probability': 0.86
    },
    'Urinary Tract Infection': {
        'symptoms': ['burning_urination', 'frequent_urination', 'abdominal_pain', 'blood_in_urine', 'fever'],
        'probability': 0.88
    },
    'Migraine': {
        'symptoms': ['severe_headache', 'nausea', 'vomiting', 'sensitivity_to_light', 'dizziness'],
        'probability': 0.85
    },
    'Type 2 Diabetes': {
        'symptoms': ['increased_thirst', 'frequent_urination', 'fatigue', 'blurred_vision', 'slow_healing', 'weight_loss'],
        'probability': 0.80
    },
    'Hypertension': {
        'symptoms': ['headache', 'dizziness', 'chest_pain', 'shortness_of_breath', 'nosebleeds'],
        'probability': 0.75
    },
    'Anxiety Disorder': {
        'symptoms': ['anxiety', 'rapid_heartbeat', 'sweating', 'insomnia', 'fatigue', 'difficulty_concentrating'],
        'probability': 0.82
    },
    'Depression': {
        'symptoms': ['depression', 'fatigue', 'loss_of_appetite', 'insomnia', 'loss_of_interest', 'weight_changes'],
        'probability': 0.80
    },
    'Arthritis': {
        'symptoms': ['joint_pain', 'stiffness', 'swelling', 'limited_range_of_motion', 'fatigue'],
        'probability': 0.84
    },
    'Food Poisoning': {
        'symptoms': ['nausea', 'vomiting', 'diarrhea', 'abdominal_pain', 'fever', 'weakness'],
        'probability': 0.89
    }
}

# Generate synthetic dataset
data = []
np.random.seed(42)

for disease, info in disease_patterns.items():
    # Generate 150 samples per disease for training
    for _ in range(150):
        sample = {symptom: 0 for symptom in symptoms_list}
        
        # Add primary symptoms with high probability
        for symptom in info['symptoms']:
            if symptom in symptoms_list:
                sample[symptom] = 1
        
        # Add some random symptoms (noise) with low probability
        for symptom in symptoms_list:
            if sample[symptom] == 0 and np.random.random() < 0.1:
                sample[symptom] = 1
        
        # Remove some primary symptoms occasionally (to simulate variation)
        for symptom in info['symptoms']:
            if symptom in symptoms_list and sample[symptom] == 1:
                if np.random.random() < (1 - info['probability']):
                    sample[symptom] = 0
        
        sample['disease'] = disease
        data.append(sample)

# Create DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv('disease_dataset.csv', index=False)
print(f"Dataset created with {len(df)} samples and {len(disease_patterns)} diseases")
print(f"\nDisease distribution:")
print(df['disease'].value_counts())

# Train the model
X = df.drop('disease', axis=1)
y = df['disease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=200, random_state=42, max_depth=20)
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Save model
with open('disease_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save symptom list
with open('symptoms_list.pkl', 'wb') as f:
    pickle.dump(symptoms_list, f)

print("\nModel and data saved successfully!")

print("Files created: disease_dataset.csv, disease_model.pkl, symptoms_list.pkl")
