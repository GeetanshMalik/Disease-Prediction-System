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

# Load model and data
@st.cache_resource
def load_model_data():
    try:
        with open('disease_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('symptoms_list.pkl', 'rb') as f:
            symptoms_list = pickle.load(f)
        return model, symptoms_list
    except FileNotFoundError:
        st.error("Model files not found! Please run the dataset generator first.")
        st.stop()

# Initialize
try:
    model, symptoms_list = load_model_data()
except:
    st.error("⚠️ Please run 'python disease_dataset_generator.py' first to create the model!")
    st.stop()

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
    This system uses Machine Learning to predict possible diseases based on your symptoms.
    
    **Features:**
    - AI-powered disease prediction
    - Safe OTC medicine recommendations
    - Prescription medicine information
    - Home remedies
    - Dietary suggestions
    
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

# Create symptom selection in columns
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

# Initialize session state
if 'selected_symptoms' not in st.session_state:
    st.session_state.selected_symptoms = []

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
        
        # Prepare input for model
        input_data = np.zeros(len(symptoms_list))
        for symptom in selected_symptoms:
            if symptom in symptoms_list:
                input_data[symptoms_list.index(symptom)] = 1
        
        # Make prediction
        prediction = model.predict([input_data])[0]
        prediction_proba = model.predict_proba([input_data])[0]
        
        # Get top 3 predictions
        top_3_indices = np.argsort(prediction_proba)[-3:][::-1]
        top_3_diseases = [model.classes_[i] for i in top_3_indices]
        top_3_probabilities = [prediction_proba[i] for i in top_3_indices]
        
        # Display predictions
        st.markdown("### 🏥 Possible Diseases (Ranked by Probability)")
        
        for i, (disease, probability) in enumerate(zip(top_3_diseases, top_3_probabilities)):
            if probability > 0.05:  # Only show if probability > 5%
                with st.container():
                    if i == 0:
                        st.markdown(f"<div class='disease-card'><h3>🥇 Most Likely: {disease}</h3><p>Confidence: {probability*100:.1f}%</p></div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div class='info-section'><h4>#{i+1}: {disease}</h4><p>Confidence: {probability*100:.1f}%</p></div>", unsafe_allow_html=True)
                    
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
    <p>🏥 AI Disease Prediction System | Built with Machine Learning & Streamlit</p>
    <p><small>Trained on comprehensive symptom-disease patterns | Model Accuracy: ~85%</small></p>
    <p><strong>Created by: Geetansh Malik</strong></p>
    <p style='font-size: 0.9em; margin-top: 0.5rem;'>💻 Developed with ❤️ using Python, Scikit-learn & Streamlit</p>
</div>
""", unsafe_allow_html=True)
