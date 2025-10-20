import streamlit as st
import pickle
import numpy as np
import pandas as pd
from disease_info import get_disease_info, get_all_diseases

# Page configuration
st.set_page_config(
    page_title="AI Disease Prediction System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .symptom-card {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .disease-card {
        background-color: #fff5ee;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #ff6347;
        color: #1e1e1e;
    }
    .info-section {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        color: #1e1e1e;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
    }
    h2 {
        color: #34495e;
    }
    h3 {
        color: #e74c3c;
    }
    .warning {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
        color: #1e1e1e;
    }
    .success {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
        color: #1e1e1e;
    }
    .final-note {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        color: #1e1e1e;
    }
    </style>
""", unsafe_allow_html=True)

# Comprehensive Disease Knowledge Base
@st.cache_resource
def load_disease_knowledge():
    """Load comprehensive disease-symptom knowledge base"""
    
    # Complete symptom list
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
    
    # Professional medical knowledge base with weighted symptoms
    disease_knowledge = {
        'Common Cold': {
            'critical': {'runny_nose': 10, 'sneezing': 10, 'sore_throat': 9},
            'major': {'cough': 8, 'headache': 6, 'body_ache': 5},
            'minor': {'fatigue': 4, 'fever': 3},
            'negative': {'loss_of_taste': -10, 'loss_of_smell': -10, 'difficulty_breathing': -8, 'wheezing': -8}
        },
        'Influenza (Flu)': {
            'critical': {'fever': 10, 'body_ache': 10, 'chills': 9},
            'major': {'cough': 8, 'fatigue': 8, 'headache': 7, 'sore_throat': 6},
            'minor': {'muscle_weakness': 4, 'sweating': 3},
            'negative': {'diarrhea': -5, 'rash': -8, 'itching': -8}
        },
        'COVID-19': {
            'critical': {'fever': 9, 'cough': 9, 'loss_of_taste': 10, 'loss_of_smell': 10},
            'major': {'fatigue': 8, 'difficulty_breathing': 9, 'body_ache': 7},
            'minor': {'headache': 5, 'sore_throat': 5, 'diarrhea': 4},
            'negative': {'itching': -8, 'rash': -6}
        },
        'Allergic Rhinitis': {
            'critical': {'sneezing': 10, 'runny_nose': 10, 'watery_eyes': 10},
            'major': {'itching': 8, 'headache': 5},
            'minor': {'fatigue': 3},
            'negative': {'fever': -10, 'body_ache': -10, 'chills': -10, 'loss_of_taste': -10}
        },
        'Asthma': {
            'critical': {'wheezing': 10, 'shortness_of_breath': 10, 'difficulty_breathing': 10},
            'major': {'chest_pain': 8, 'cough': 7},
            'minor': {'fatigue': 3},
            'negative': {'fever': -10, 'runny_nose': -8, 'sneezing': -8, 'diarrhea': -10, 'vomiting': -10}
        },
        'Bronchitis': {
            'critical': {'persistent_cough': 10, 'chest_pain': 9},
            'major': {'fatigue': 7, 'shortness_of_breath': 8, 'body_ache': 6},
            'minor': {'fever': 4, 'headache': 3},
            'negative': {'diarrhea': -10, 'vomiting': -8, 'rash': -8}
        },
        'Gastroenteritis': {
            'critical': {'diarrhea': 10, 'vomiting': 10, 'nausea': 10},
            'major': {'abdominal_pain': 9, 'fever': 6, 'loss_of_appetite': 7},
            'minor': {'fatigue': 5, 'body_ache': 3},
            'negative': {'cough': -10, 'runny_nose': -10, 'chest_pain': -10, 'wheezing': -10}
        },
        'Urinary Tract Infection': {
            'critical': {'burning_urination': 10, 'frequent_urination': 10},
            'major': {'abdominal_pain': 8, 'back_pain': 8, 'blood_in_urine': 9},
            'minor': {'fever': 5, 'fatigue': 4},
            'negative': {'cough': -10, 'runny_nose': -10, 'diarrhea': -8, 'vomiting': -8}
        },
        'Migraine': {
            'critical': {'headache': 10},
            'major': {'nausea': 8, 'dizziness': 8, 'vomiting': 7},
            'minor': {'fatigue': 5, 'blurred_vision': 6},
            'negative': {'fever': -8, 'cough': -10, 'runny_nose': -10, 'diarrhea': -10}
        },
        'Type 2 Diabetes': {
            'critical': {'increased_thirst': 10, 'frequent_urination': 10},
            'major': {'fatigue': 8, 'blurred_vision': 9, 'weight_loss': 8, 'slow_healing': 8},
            'minor': {'frequent_urination': 6},
            'negative': {'fever': -10, 'cough': -10, 'runny_nose': -10, 'acute_symptoms': -10}
        },
        'Hypertension': {
            'critical': {'headache': 8, 'dizziness': 8},
            'major': {'chest_pain': 9, 'shortness_of_breath': 7, 'blurred_vision': 7},
            'minor': {'fatigue': 5, 'rapid_heartbeat': 6},
            'negative': {'fever': -10, 'cough': -10, 'diarrhea': -10, 'vomiting': -10}
        },
        'Anxiety Disorder': {
            'critical': {'anxiety': 10, 'rapid_heartbeat': 9},
            'major': {'sweating': 8, 'insomnia': 8, 'dizziness': 7},
            'minor': {'fatigue': 6, 'headache': 5},
            'negative': {'fever': -10, 'cough': -10, 'vomiting': -10, 'diarrhea': -10}
        },
        'Depression': {
            'critical': {'depression': 10, 'fatigue': 9, 'insomnia': 9},
            'major': {'loss_of_appetite': 8, 'weight_loss': 7, 'anxiety': 6},
            'minor': {'body_ache': 4, 'headache': 4},
            'negative': {'fever': -10, 'cough': -10, 'vomiting': -10, 'diarrhea': -10}
        },
        'Arthritis': {
            'critical': {'joint_pain': 10},
            'major': {'fatigue': 7, 'muscle_weakness': 6, 'back_pain': 7},
            'minor': {'headache': 3},
            'negative': {'fever': -8, 'cough': -10, 'diarrhea': -10, 'vomiting': -10}
        },
        'Food Poisoning': {
            'critical': {'nausea': 10, 'vomiting': 10, 'diarrhea': 10},
            'major': {'abdominal_pain': 9, 'fever': 6},
            'minor': {'fatigue': 5, 'body_ache': 4},
            'negative': {'cough': -10, 'runny_nose': -10, 'chest_pain': -10, 'joint_pain': -10}
        }
    }
    
    return symptoms_list, disease_knowledge

def calculate_disease_match(selected_symptoms, disease_name, disease_data):
    """Advanced scoring algorithm for disease matching"""
    score = 0
    max_possible_score = 0
    
    # Calculate scores for each symptom category
    for category in ['critical', 'major', 'minor']:
        if category in disease_data:
            for symptom, weight in disease_data[category].items():
                max_possible_score += weight
                if symptom in selected_symptoms:
                    score += weight
    
    # Apply negative scoring for conflicting symptoms
    if 'negative' in disease_data:
        for symptom, penalty in disease_data['negative'].items():
            if symptom in selected_symptoms:
                score += penalty  # Negative value
    
    # Calculate confidence percentage
    if max_possible_score > 0:
        confidence = (score / max_possible_score) * 100
        confidence = max(0, min(100, confidence))  # Cap between 0-100
    else:
        confidence = 0
    
    return confidence

# Load knowledge base
symptoms_list, disease_knowledge = load_disease_knowledge()

# Title and description
st.markdown("<h1>🏥 AI-Powered Disease Prediction System</h1>", unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.info("💡 Select your symptoms below and get instant AI-powered predictions with treatment recommendations")

# Sidebar
with st.sidebar:
    st.header("📋 About")
    st.write("""
    This system uses advanced Medical AI to predict possible diseases based on your symptoms.
    
    **Features:**
    - Professional medical knowledge base
    - Weighted symptom analysis
    - Treatment recommendations
    - Home remedies & diet plans
    
    **Developer:** Geetansh Malik
    """)
    
    st.warning("⚠️ **Disclaimer**: This is an AI-based educational tool. Always consult healthcare professionals for proper diagnosis and treatment.")
    
    st.markdown("---")
    st.markdown("### 🩺 Emergency Numbers")
    st.markdown("**India**: 108 (Ambulance)")
    st.markdown("**USA**: 911")
    st.markdown("**UK**: 999")

# Main content
st.markdown("## Select Your Symptoms")
st.markdown("Choose all symptoms you are currently experiencing:")

# Symptom selection with better organization
symptom_readable = {
    'fever': '🌡️ Fever',
    'cough': '😷 Cough',
    'fatigue': '😫 Fatigue/Tiredness',
    'difficulty_breathing': '🫁 Difficulty Breathing',
    'sore_throat': '🗣️ Sore Throat',
    'runny_nose': '👃 Runny Nose',
    'headache': '🤕 Headache',
    'body_ache': '💪 Body Ache',
    'chills': '🥶 Chills',
    'nausea': '🤢 Nausea',
    'vomiting': '🤮 Vomiting',
    'diarrhea': '💩 Diarrhea',
    'loss_of_taste': '👅 Loss of Taste',
    'loss_of_smell': '👃 Loss of Smell',
    'chest_pain': '❤️ Chest Pain',
    'rapid_heartbeat': '💓 Rapid Heartbeat',
    'dizziness': '😵 Dizziness',
    'sweating': '💦 Excessive Sweating',
    'abdominal_pain': '🤰 Abdominal Pain',
    'bloating': '🎈 Bloating',
    'constipation': '🚽 Constipation',
    'joint_pain': '🦴 Joint Pain',
    'muscle_weakness': '💪 Muscle Weakness',
    'rash': '🔴 Skin Rash',
    'itching': '😖 Itching',
    'sneezing': '🤧 Sneezing',
    'watery_eyes': '😭 Watery Eyes',
    'wheezing': '🌬️ Wheezing',
    'shortness_of_breath': '😮‍💨 Shortness of Breath',
    'back_pain': '🔙 Back Pain',
    'frequent_urination': '🚻 Frequent Urination',
    'burning_urination': '🔥 Burning During Urination',
    'blood_in_urine': '💉 Blood in Urine',
    'weight_loss': '⚖️ Unexplained Weight Loss',
    'increased_thirst': '🥤 Increased Thirst',
    'blurred_vision': '👓 Blurred Vision',
    'slow_healing': '🩹 Slow Healing of Wounds',
    'anxiety': '😰 Anxiety',
    'depression': '😔 Depression/Sadness',
    'insomnia': '😴 Insomnia/Sleep Problems',
    'loss_of_appetite': '🍽️ Loss of Appetite',
    'weight_gain': '⚖️ Weight Gain',
    'swollen_lymph_nodes': '🔴 Swollen Lymph Nodes',
    'night_sweats': '🌙 Night Sweats',
    'persistent_cough': '😷 Persistent Cough (>3 weeks)'
}

# Create 3 columns for symptom checkboxes
cols = st.columns(3)
selected_symptoms = []

for idx, (symptom, label) in enumerate(symptom_readable.items()):
    col_idx = idx % 3
    with cols[col_idx]:
        if st.checkbox(label, key=symptom):
            selected_symptoms.append(symptom)

st.markdown("---")

# Prediction button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    predict_button = st.button("🔍 Predict Disease", use_container_width=True)

# Prediction logic
if predict_button:
    if len(selected_symptoms) == 0:
        st.error("⚠️ Please select at least one symptom!")
    else:
        st.markdown("---")
        st.markdown("## 🎯 Prediction Results")
        
        # Show selected symptoms
        with st.expander("📝 Selected Symptoms", expanded=True):
            symptoms_text = ", ".join([symptom_readable[s] for s in selected_symptoms])
            st.write(symptoms_text)
        
        # Calculate match for all diseases
        disease_scores = []
        for disease_name, disease_data in disease_knowledge.items():
            confidence = calculate_disease_match(selected_symptoms, disease_name, disease_data)
            if confidence > 15:  # Only show if confidence > 15%
                disease_scores.append((disease_name, confidence))
        
        # Sort by confidence
        disease_scores.sort(key=lambda x: x[1], reverse=True)
        
        if len(disease_scores) == 0:
            st.warning("⚠️ No strong disease match found with the selected symptoms. Please consult a doctor for proper diagnosis.")
        else:
            # Get top 3 predictions
            top_predictions = disease_scores[:min(3, len(disease_scores))]
            
            st.markdown("### 🏥 Possible Diseases (Ranked by Confidence)")
            
            for i, (disease, confidence) in enumerate(top_predictions):
                with st.container():
                    if i == 0:
                        st.markdown(f"<div class='disease-card'><h3>🥇 Most Likely: {disease}</h3><p>Confidence: {confidence:.1f}%</p></div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div class='info-section'><h4>#{i+1}: {disease}</h4><p>Confidence: {confidence:.1f}%</p></div>", unsafe_allow_html=True)
                    
                    # Get disease information
                    disease_info = get_disease_info(disease)
                    
                    if disease_info:
                        # Create tabs for different information
                        tab1, tab2, tab3, tab4, tab5 = st.tabs([
                            "📖 About", 
                            "💊 OTC Medicines", 
                            "⚕️ Prescription Info",
                            "🏠 Home Remedies",
                            "🥗 Diet Recommendations"
                        ])
                        
                        with tab1:
                            st.write(f"**Description:** {disease_info['description']}")
                        
                        with tab2:
                            st.markdown("**✅ Safe Over-The-Counter Medicines:**")
                            for medicine in disease_info['otc_medicines']:
                                st.markdown(f"- {medicine}")
                            st.info("💡 These medicines are generally safe but always read labels and follow dosage instructions.")
                        
                        with tab3:
                            st.markdown("**⚕️ Prescription Medicines (Require Doctor Consultation):**")
                            for medicine in disease_info['prescription_medicines']:
                                st.markdown(f"- {medicine}")
                            st.warning("⚠️ DO NOT self-medicate with prescription drugs. Consult a healthcare professional.")
                        
                        with tab4:
                            st.markdown("**🏠 Home Remedies & Self-Care:**")
                            for remedy in disease_info['home_remedies']:
                                st.markdown(f"- {remedy}")
                        
                        with tab5:
                            st.markdown("**🥗 Recommended Foods & Diet:**")
                            for diet_item in disease_info['diet']:
                                st.markdown(f"- {diet_item}")
                    
                    st.markdown("---")
            
            # General recommendations
            st.markdown("## 📌 General Recommendations")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                <div class='success'>
                <h4>✅ Do's</h4>
                <ul>
                    <li>Stay hydrated - drink plenty of water</li>
                    <li>Get adequate rest (7-9 hours sleep)</li>
                    <li>Maintain good hygiene</li>
                    <li>Eat nutritious, balanced meals</li>
                    <li>Monitor your symptoms</li>
                    <li>Follow medication instructions carefully</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class='warning'>
                <h4>⚠️ When to Seek Immediate Medical Help</h4>
                <ul>
                    <li>Difficulty breathing or chest pain</li>
                    <li>High fever (>103°F/39.4°C)</li>
                    <li>Severe pain or discomfort</li>
                    <li>Symptoms worsen or don't improve</li>
                    <li>Signs of dehydration</li>
                    <li>Confusion or altered mental state</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("""
            <div class='final-note'>
            <h4>💙 Remember: This is an AI prediction tool for educational purposes only</h4>
            <p>For accurate diagnosis and treatment, please consult a qualified healthcare professional</p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 2rem 0;'>
    <p>🏥 AI Disease Prediction System | Built with Advanced Medical AI</p>
    <p><small>Professional medical knowledge base with weighted symptom analysis</small></p>
    <p><strong>Created by: Geetansh Malik</strong></p>
    <p style='font-size: 0.9em; margin-top: 0.5rem;'>💻 Developed with ❤️ using Python & Streamlit</p>
</div>
""", unsafe_allow_html=True)
