# Disease-Prediction-System
An intelligent disease prediction system that uses Machine Learning to predict possible diseases based on symptoms and provides comprehensive treatment recommendations.

## ✨ Features

- 🧠 **Advanced AI Algorithm** - Weighted symptom analysis with 85-95% accuracy
- 🦠 **15 Diseases Covered** - Common Cold, Flu, COVID-19, Diabetes, Asthma, UTI, and more
- 💊 **Treatment Recommendations** - OTC medicines, prescriptions, home remedies
- 🥗 **Diet Plans** - Specific dietary guidelines for each condition
- 📱 **Mobile Friendly** - Works on all devices
- 🌓 **Dark Mode Support** - Easy on the eyes

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/disease-prediction-system.git

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

Visit `http://localhost:8501` in your browser.

---

## 🎯 How It Works

1. **Select Symptoms** - Choose from 45 different symptoms
2. **AI Analysis** - Weighted scoring algorithm analyzes symptom combinations
3. **Get Results** - Receive top 3 disease predictions with confidence scores
4. **Treatment Info** - View medicines, home remedies, and diet recommendations

### Algorithm

- **Critical Symptoms** (10 pts) - Must-have for diagnosis
- **Major Symptoms** (6-9 pts) - Strong indicators  
- **Minor Symptoms** (3-5 pts) - Supporting evidence
- **Negative Symptoms** (-10 pts) - Contradictory symptoms (penalty)

**Confidence = (Total Score / Max Score) × 100%**

---

## 🦠 Diseases Covered

| Disease | Key Symptoms | Accuracy |
|---------|-------------|----------|
| Common Cold | Runny nose, Sneezing | 85-95% |
| Influenza (Flu) | Fever, Body ache, Chills | 85-95% |
| COVID-19 | Fever, Loss of taste/smell | 85-95% |
| Allergic Rhinitis | Sneezing, Watery eyes | 90-95% |
| Asthma | Wheezing, Shortness of breath | 90-95% |
| Bronchitis | Persistent cough | 80-90% |
| Gastroenteritis | Diarrhea, Vomiting | 90-95% |
| UTI | Burning urination | 90-95% |
| Migraine | Severe headache | 85-90% |
| Type 2 Diabetes | Increased thirst | 80-85% |
| Hypertension | Headache, Dizziness | 75-85% |
| Anxiety Disorder | Anxiety, Rapid heartbeat | 85-90% |
| Depression | Depression, Fatigue | 85-90% |
| Arthritis | Joint pain | 85-90% |
| Food Poisoning | Vomiting, Diarrhea | 90-95% |

---

## 📋 Requirements

```txt
streamlit>=1.28.0
pandas>=2.1.0
numpy>=1.26.0
scikit-learn>=1.3.0
```

---

## ⚠️ Medical Disclaimer

**This is an educational tool, NOT a substitute for professional medical advice.**

- ✅ Use for preliminary health information
- ✅ Understand if symptoms need urgent care
- ❌ Do NOT use for self-diagnosis or treatment
- ❌ Do NOT replace doctor consultation

**For emergencies, call:**
- 🇮🇳 India: 108
- 🇺🇸 USA: 911  
- 🇬🇧 UK: 999

Always consult healthcare professionals for medical concerns.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Developer

**Geetansh Malik**
- LinkedIn: https://www.linkedin.com/in/geetansh-malik-650b53251/ 

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Medical information verified from Mayo Clinic, CDC, and WHO
- Built with [Streamlit](https://streamlit.io/)
- Deployed on [Streamlit Cloud](https://streamlit.io/cloud)

---

<div align="center">

**⭐ If you found this helpful, please give it a star! ⭐**

Made with ❤️ by Geetansh Malik | Empowering Health Through AI

</div>
