# disease_info.py - Comprehensive disease information database

DISEASE_INFO = {
    'Common Cold': {
        'description': 'A viral infection of the upper respiratory tract that is usually harmless.',
        'otc_medicines': [
            'Paracetamol/Acetaminophen (for fever and pain)',
            'Ibuprofen (for pain and inflammation)',
            'Decongestant nasal sprays (short-term use)',
            'Antihistamines (for runny nose)',
            'Cough syrup with dextromethorphan'
        ],
        'prescription_medicines': [
            'Usually not required',
            'Antibiotics only if bacterial infection develops'
        ],
        'home_remedies': [
            'Drink plenty of warm fluids (water, herbal tea, warm lemon water)',
            'Gargle with warm salt water for sore throat',
            'Use a humidifier to ease congestion',
            'Get adequate rest (7-9 hours sleep)',
            'Steam inhalation with eucalyptus oil',
            'Honey and ginger tea'
        ],
        'diet': [
            'Vitamin C rich foods: Oranges, strawberries, bell peppers',
            'Zinc rich foods: Nuts, seeds, legumes',
            'Warm soups and broths',
            'Garlic (natural antimicrobial)',
            'Turmeric milk (anti-inflammatory)',
            'Avoid dairy if it increases mucus production'
        ]
    },
    
    'Influenza (Flu)': {
        'description': 'A contagious respiratory illness caused by influenza viruses.',
        'otc_medicines': [
            'Paracetamol/Acetaminophen (fever reducer)',
            'Ibuprofen (pain and fever relief)',
            'Decongestants',
            'Cough suppressants'
        ],
        'prescription_medicines': [
            'Oseltamivir (Tamiflu) - antiviral medication',
            'Zanamivir (Relenza) - antiviral medication',
            'Required if high-risk patient or severe symptoms'
        ],
        'home_remedies': [
            'Complete bed rest',
            'Drink lots of fluids (8-10 glasses daily)',
            'Warm compress for aches',
            'Steam inhalation',
            'Honey for cough relief',
            'Vitamin C supplements'
        ],
        'diet': [
            'Protein-rich foods: Eggs, chicken, fish',
            'Vitamin E: Almonds, sunflower seeds',
            'Probiotics: Yogurt, kefir',
            'Ginger and turmeric',
            'Green leafy vegetables',
            'Stay hydrated with electrolyte drinks'
        ]
    },
    
    'COVID-19': {
        'description': 'Respiratory illness caused by SARS-CoV-2 virus.',
        'otc_medicines': [
            'Paracetamol (for fever)',
            'Vitamin D3 supplements',
            'Vitamin C supplements',
            'Zinc supplements',
            'Throat lozenges'
        ],
        'prescription_medicines': [
            'Consult doctor immediately if symptoms worsen',
            'Paxlovid (Nirmatrelvir/Ritonavir) - for high-risk patients',
            'Remdesivir - for hospitalized patients',
            'Corticosteroids if oxygen levels drop',
            'Antibiotics only if secondary bacterial infection'
        ],
        'home_remedies': [
            'Self-isolate for 5-10 days',
            'Monitor oxygen levels with pulse oximeter',
            'Prone positioning (lying on stomach)',
            'Deep breathing exercises',
            'Steam inhalation',
            'Plenty of rest and fluids'
        ],
        'diet': [
            'High protein diet for recovery',
            'Vitamin C rich fruits',
            'Zinc rich foods',
            'Omega-3 fatty acids: Fish, flaxseeds',
            'Antioxidant-rich foods: Berries, green tea',
            'Easily digestible foods if appetite is low'
        ]
    },
    
    'Allergic Rhinitis': {
        'description': 'Inflammation of nasal passages due to allergens.',
        'otc_medicines': [
            'Cetirizine (antihistamine)',
            'Loratadine (antihistamine)',
            'Fexofenadine (antihistamine)',
            'Nasal saline sprays',
            'Eye drops for itchy eyes'
        ],
        'prescription_medicines': [
            'Nasal corticosteroid sprays (Fluticasone, Mometasone)',
            'Leukotriene inhibitors (Montelukast)',
            'Immunotherapy if severe'
        ],
        'home_remedies': [
            'Avoid allergen triggers',
            'Use air purifiers',
            'Nasal irrigation with saline solution',
            'Keep windows closed during high pollen days',
            'Shower after being outdoors',
            'Local honey (may help with pollen allergies)'
        ],
        'diet': [
            'Quercetin-rich foods: Apples, onions, berries',
            'Omega-3 fatty acids: Fish, walnuts',
            'Probiotic foods: Yogurt, kimchi',
            'Vitamin C foods',
            'Avoid foods that may trigger histamine: aged cheese, wine',
            'Green tea (natural antihistamine)'
        ]
    },
    
    'Asthma': {
        'description': 'Chronic condition causing airway inflammation and breathing difficulty.',
        'otc_medicines': [
            'Avoid self-medication',
            'Over-the-counter options limited'
        ],
        'prescription_medicines': [
            'Quick-relief inhaler (Albuterol/Salbutamol) - REQUIRED',
            'Long-term control inhalers (Corticosteroids)',
            'Leukotriene modifiers',
            'Combination inhalers',
            'DOCTOR CONSULTATION ESSENTIAL'
        ],
        'home_remedies': [
            'Breathing exercises (pursed-lip breathing)',
            'Avoid triggers (smoke, dust, cold air)',
            'Use air purifier',
            'Maintain ideal humidity levels',
            'Stay warm in cold weather',
            'Practice yoga and meditation'
        ],
        'diet': [
            'Vitamin D rich foods: Fatty fish, fortified milk',
            'Magnesium rich foods: Spinach, pumpkin seeds',
            'Beta-carotene foods: Carrots, sweet potatoes',
            'Omega-3 fatty acids',
            'Avoid sulfites (dried fruits, wine)',
            'Avoid allergenic foods if identified'
        ]
    },
    
    'Bronchitis': {
        'description': 'Inflammation of the bronchial tubes carrying air to lungs.',
        'otc_medicines': [
            'Paracetamol for fever',
            'Expectorant cough syrup (Guaifenesin)',
            'Throat lozenges',
            'Steam inhalers'
        ],
        'prescription_medicines': [
            'Antibiotics (if bacterial infection confirmed)',
            'Bronchodilators for breathing difficulty',
            'Cough suppressants (if prescribed)',
            'Inhaled corticosteroids if chronic'
        ],
        'home_remedies': [
            'Drink warm fluids frequently',
            'Use a humidifier',
            'Honey and lemon tea',
            'Steam inhalation 2-3 times daily',
            'Avoid smoke and irritants',
            'Rest and avoid strenuous activity'
        ],
        'diet': [
            'Anti-inflammatory foods: Turmeric, ginger',
            'Vitamin C rich foods',
            'Garlic (antimicrobial properties)',
            'Warm soups and broths',
            'Herbal teas (thyme, peppermint)',
            'Avoid mucus-producing foods if they worsen symptoms'
        ]
    },
    
    'Gastroenteritis': {
        'description': 'Inflammation of stomach and intestines, often called stomach flu.',
        'otc_medicines': [
            'Oral rehydration solutions (ORS)',
            'Loperamide (for diarrhea, use cautiously)',
            'Bismuth subsalicylate (Pepto-Bismol)',
            'Anti-nausea medications',
            'Probiotics'
        ],
        'prescription_medicines': [
            'Antibiotics (only if bacterial cause confirmed)',
            'Anti-parasitic medications (if parasitic infection)',
            'IV fluids if severe dehydration',
            'Prescription anti-nausea medications'
        ],
        'home_remedies': [
            'Stay hydrated - sip fluids frequently',
            'BRAT diet (Bananas, Rice, Applesauce, Toast)',
            'Ginger tea for nausea',
            'Peppermint tea',
            'Rest completely',
            'Avoid solid foods initially'
        ],
        'diet': [
            'Clear liquids initially: Water, broth, clear juices',
            'Gradually add bland foods',
            'Bananas (potassium)',
            'Rice and toast',
            'Plain crackers',
            'AVOID: Dairy, fatty foods, caffeine, alcohol, spicy foods for 24-48 hours'
        ]
    },
    
    'Urinary Tract Infection': {
        'description': 'Bacterial infection affecting the urinary system.',
        'otc_medicines': [
            'Phenazopyridine (for pain relief)',
            'Cranberry supplements',
            'Increased water intake (not medicine but critical)'
        ],
        'prescription_medicines': [
            'Antibiotics REQUIRED - Trimethoprim/Sulfamethoxazole',
            'Nitrofurantoin',
            'Ciprofloxacin',
            'Cephalexin',
            'MUST CONSULT DOCTOR - Don\'t delay treatment'
        ],
        'home_remedies': [
            'Drink 8-10 glasses of water daily',
            'Urinate frequently, don\'t hold urine',
            'Wipe front to back',
            'Avoid irritants: perfumed products',
            'Apply heating pad to lower abdomen',
            'Cranberry juice (unsweetened)'
        ],
        'diet': [
            'Plenty of water',
            'Cranberry juice or supplements',
            'Vitamin C rich foods (acidify urine)',
            'Probiotic yogurt',
            'Avoid: Caffeine, alcohol, spicy foods, artificial sweeteners',
            'Cucumber, watermelon (high water content)'
        ]
    },
    
    'Migraine': {
        'description': 'Severe recurring headache, often with nausea and light sensitivity.',
        'otc_medicines': [
            'Ibuprofen',
            'Paracetamol/Acetaminophen',
            'Aspirin',
            'Caffeine combinations (Excedrin)',
            'Take at first sign of migraine'
        ],
        'prescription_medicines': [
            'Triptans (Sumatriptan, Rizatriptan)',
            'Preventive medications: Beta-blockers, Antidepressants',
            'CGRP inhibitors (newer treatments)',
            'Anti-nausea medications',
            'Consult neurologist for chronic migraines'
        ],
        'home_remedies': [
            'Rest in dark, quiet room',
            'Cold compress on forehead',
            'Peppermint oil on temples',
            'Ginger tea for nausea',
            'Maintain sleep schedule',
            'Avoid triggers (keep diary)'
        ],
        'diet': [
            'Magnesium rich foods: Almonds, spinach',
            'Riboflavin (B2): Eggs, green vegetables',
            'Stay hydrated',
            'Regular meal schedule',
            'Avoid triggers: Aged cheese, processed meats, MSG, alcohol',
            'Limit caffeine intake (consistent amounts)'
        ]
    },
    
    'Type 2 Diabetes': {
        'description': 'Chronic condition affecting blood sugar regulation.',
        'otc_medicines': [
            'Blood glucose monitor (essential)',
            'Not treated with OTC medicines',
            'Chromium supplements (consult doctor)'
        ],
        'prescription_medicines': [
            'Metformin (first-line treatment)',
            'Sulfonylureas',
            'DPP-4 inhibitors',
            'SGLT2 inhibitors',
            'Insulin (if required)',
            'REQUIRES ONGOING MEDICAL SUPERVISION'
        ],
        'home_remedies': [
            'Regular exercise (30 min/day)',
            'Weight management',
            'Monitor blood sugar regularly',
            'Stress management',
            'Adequate sleep',
            'Cinnamon (may help blood sugar)'
        ],
        'diet': [
            'Low glycemic index foods',
            'High fiber foods: Whole grains, vegetables',
            'Lean proteins: Fish, chicken',
            'Healthy fats: Nuts, avocado',
            'Portion control',
            'AVOID: Sugary drinks, white bread, refined carbs',
            'Regular meal timing'
        ]
    },
    
    'Hypertension': {
        'description': 'High blood pressure, often called the silent killer.',
        'otc_medicines': [
            'Blood pressure monitor (essential)',
            'Garlic supplements (consult doctor)',
            'Coenzyme Q10 (consult doctor)',
            'Not typically treated with OTC medicines'
        ],
        'prescription_medicines': [
            'ACE inhibitors',
            'Angiotensin II receptor blockers (ARBs)',
            'Calcium channel blockers',
            'Diuretics',
            'Beta-blockers',
            'REQUIRES DOCTOR CONSULTATION AND MONITORING'
        ],
        'home_remedies': [
            'Regular exercise (moderate intensity)',
            'Limit sodium intake (<2300mg/day)',
            'Maintain healthy weight',
            'Reduce stress: Meditation, yoga',
            'Limit alcohol',
            'Monitor BP regularly at home'
        ],
        'diet': [
            'DASH diet (Dietary Approaches to Stop Hypertension)',
            'Potassium rich: Bananas, potatoes, spinach',
            'Low sodium foods',
            'Whole grains',
            'Lean proteins',
            'Limit: Salt, saturated fats, processed foods',
            'Dark chocolate (small amounts)',
            'Beets, garlic'
        ]
    },
    
    'Anxiety Disorder': {
        'description': 'Mental health condition causing excessive worry and fear.',
        'otc_medicines': [
            'Herbal supplements: Chamomile, Valerian root',
            'L-theanine',
            'Magnesium supplements',
            'Lavender oil (aromatherapy)',
            'NOT a substitute for professional treatment'
        ],
        'prescription_medicines': [
            'SSRIs (Sertraline, Escitalopram)',
            'Benzodiazepines (short-term use)',
            'Buspirone',
            'Beta-blockers (for physical symptoms)',
            'THERAPY + MEDICATION recommended',
            'Consult psychiatrist or psychologist'
        ],
        'home_remedies': [
            'Deep breathing exercises',
            'Progressive muscle relaxation',
            'Regular physical exercise',
            'Mindfulness meditation',
            'Adequate sleep (7-9 hours)',
            'Limit caffeine and alcohol',
            'Journaling'
        ],
        'diet': [
            'Omega-3 fatty acids: Fatty fish, walnuts',
            'Complex carbohydrates: Whole grains',
            'Protein at each meal',
            'Magnesium rich foods',
            'B-vitamins: Leafy greens, legumes',
            'Limit: Caffeine, sugar, processed foods',
            'Stay hydrated',
            'Chamomile tea'
        ]
    },
    
    'Depression': {
        'description': 'Mental health condition causing persistent sadness and loss of interest.',
        'otc_medicines': [
            'St. John\'s Wort (consult doctor - interacts with many drugs)',
            'Omega-3 supplements',
            'Vitamin D supplements',
            'SAMe supplements',
            'NOT a replacement for professional treatment'
        ],
        'prescription_medicines': [
            'SSRIs (Fluoxetine, Sertraline)',
            'SNRIs (Venlafaxine, Duloxetine)',
            'Bupropion',
            'Tricyclic antidepressants',
            'PSYCHOTHERAPY + MEDICATION most effective',
            'SEEK PROFESSIONAL HELP - DO NOT SELF-TREAT'
        ],
        'home_remedies': [
            'Regular exercise (proven effective)',
            'Maintain sleep schedule',
            'Social connection',
            'Sunlight exposure',
            'Mindfulness and meditation',
            'Set small achievable goals',
            'Limit alcohol',
            'Support groups'
        ],
        'diet': [
            'Omega-3 rich foods: Salmon, sardines',
            'Folate rich: Spinach, lentils',
            'B12: Eggs, dairy, fortified foods',
            'Tryptophan: Turkey, nuts, seeds',
            'Complex carbohydrates',
            'Antioxidants: Berries, dark chocolate',
            'Avoid: Excessive sugar, processed foods',
            'Regular meal schedule'
        ]
    },
    
    'Arthritis': {
        'description': 'Joint inflammation causing pain and stiffness.',
        'otc_medicines': [
            'Ibuprofen (anti-inflammatory)',
            'Naproxen',
            'Paracetamol/Acetaminophen',
            'Topical NSAIDs (diclofenac gel)',
            'Glucosamine and chondroitin supplements',
            'Capsaicin cream'
        ],
        'prescription_medicines': [
            'Stronger NSAIDs',
            'Disease-modifying antirheumatic drugs (DMARDs)',
            'Corticosteroid injections',
            'Biologic response modifiers',
            'Consult rheumatologist for proper diagnosis'
        ],
        'home_remedies': [
            'Hot and cold therapy',
            'Gentle exercises and stretching',
            'Maintain healthy weight',
            'Epsom salt baths',
            'Turmeric supplements',
            'Joint protection techniques',
            'Assistive devices if needed'
        ],
        'diet': [
            'Anti-inflammatory foods: Fatty fish, berries',
            'Turmeric and ginger',
            'Garlic and onions',
            'Olive oil',
            'Nuts and seeds',
            'Green tea',
            'Avoid: Processed foods, sugar, trans fats',
            'Limit red meat and dairy if inflammation increases'
        ]
    },
    
    'Food Poisoning': {
        'description': 'Illness from consuming contaminated food or water.',
        'otc_medicines': [
            'Oral rehydration solutions',
            'Bismuth subsalicylate (Pepto-Bismol)',
            'Loperamide (use cautiously)',
            'Anti-nausea medications',
            'Activated charcoal (if early)'
        ],
        'prescription_medicines': [
            'Antibiotics (only if bacterial and severe)',
            'Antiparasitic medications (if parasitic)',
            'IV fluids (if severe dehydration)',
            'Most cases resolve without prescription medicines'
        ],
        'home_remedies': [
            'Stay hydrated - sip fluids constantly',
            'Rest completely',
            'Ginger tea for nausea',
            'Start with clear liquids',
            'Gradually introduce bland foods',
            'Avoid solid foods initially',
            'Monitor for dehydration signs'
        ],
        'diet': [
            'Clear liquids: Water, broth, herbal tea',
            'Electrolyte solutions',
            'BRAT diet: Bananas, Rice, Applesauce, Toast',
            'Plain crackers',
            'Gradually add: Plain chicken, steamed vegetables',
            'Probiotics after 24 hours',
            'AVOID for 48 hours: Dairy, fatty foods, caffeine, alcohol, spicy foods'
        ]
    }
}

def get_disease_info(disease_name):
    """Get comprehensive information about a disease"""
    return DISEASE_INFO.get(disease_name, None)

def get_all_diseases():
    """Get list of all diseases in database"""
    return list(DISEASE_INFO.keys())