# param
intermapping= {
    '12-lead ecg':['cardiac monitor'],
    'albuterol':['albuterol'],
    'aspirin':['aspirin'],
    'assist ventilation (bvm)':['bag valve mask ventilation'],
    'capnography (1) first reading':['capnography'],
    'capnography (2) seco':['capnography'],
    'capnography (2) second reading':['capnography'],
    'capnography (3) final reading':['capnography'],
    'cardiac monitor':['cardiac monitor'],
    'nasopharyngeal airway insertio':['nasopharyngeal airway'],
    'cpap':['cpap'],
    'dexamethasone (decadron)':['dexamethasone'],
    'dextrose 10%':['dextrose'],
    'dextrose 25%':['dextrose'],
    'dextrose 50%':['dextrose'],
    'dextrose 5% in 0.45% ns':['dextrose'],
    'duoneb':['albuterol','ipratropium'],
    'fentanyl':['fentanyl'],
    'glucagon':['glucagon'],
    'glutose':['oral glucose'],
    'hospital':['transport'],
    'hospital contact':['transport'],
    'intubation':['endotracheal tube'],
    'ipratropium (atrovent)':['ipratropium'],
    'iv':['normal saline'],
    'magnesium sulfate':['morphine sulfate'],
    'midazolam (versed)':['midazolam'],
    'naloxone (narcan)':['narcan'],
    'nitroglycerine':['nitroglycerine'],
    'normal saline':['normal saline'],
    'ondansetron (zofran)':['ondansetron'],
    'oral glucose':['oral glucose'],
    'oxygen':['oxygen'],
    'restraints':['physical restraint'],
    'suction':['suction the oropharynx','suction the nasopharynx'],
}

EKGdic = {
     '':'',
     'AV_Block_1st_Deg':'AV_Block-1st_Degree',
     'AV_Block_1st_Degree':'AV_Block-1st_Degree',
     'AV_Block_2nd_Degree_Type_1':'AV_Block_2nd_Degree_Type_1',
     'AV_Block_2nd_Degree_Type_2':'AV_Block_2nd_Degree_Type_2',
     'AV_Block_3rd_Degree':'AV_Block_3rd_Degree',
     'Asystole':'Asystole',
     'Artifact':'Artifact',
     'Atrial_Fibrill':'Atrial_Fibrillation',
     'Atrial_Fibrillation':'Atrial_Fibrillation',
     'Atrial_Flutter':'Atrial_Flutter',
     'Juncti':'Junctional_Rhythm',
     'Junctiona':'Junctional_Rhythm',
     'Junctional':'Junctional_Rhythm',
     'Other_(Not_Listed)':'Other_(Not_Listed)',
     'P': 'Paced_Rhythm',
     'PEA':'Pulseless_Electrical_Activity',
     'Pac':'Paced_Rhythm',
     'Paced_Rhythm':'Paced_Rhythm',
     'Premature_Ventricular_Contractions':'Premature_Ventricular_Contractions',
     'Right_Bundle_Branch_Block':'Right_Bundle_Branch_Block',
     'Left_Bundle_Branch_Block':'Left_Bundle_Branch_Block',
     'STEMI_Anterior_Ischemia':'STEMI_Anterior_Ischemia',
     'STEMI_Lateral_Ischemia':'STEMI_Lateral_Ischemia',
     'STEMI_Inferior_Ischemia':'STEMI_Inferior_Ischemia',
     'S':'Sinus_Rhythm',
     'Si':'Sinus_Rhythm',
     'Sin':'Sinus_Rhythm',
     'Sinu':'Sinus_Rhythm',
     'Sinus':'Sinus_Rhythm',
     'Sinus_':'Sinus_Rhythm',
     'Sinus_Arrhythmia':'Sinus_Arrhythmia',
     'Sinus_Bradycardia':'Sinus_Bradycardia',
     'Sinus_R':'Sinus_Rhythm',
     'Sinus_Rh':'Sinus_Rhythm',
     'Sinus_Rhy':'Sinus_Rhythm',
     'Sinus_Rhyth':'Sinus_Rhythm',
     'Sinus_Rhythm':'Sinus_Rhythm',
     'Sinus_Rhythm,Sinus_Tachycardia':'Sinus_Rhythm,Sinus_Tachycardia',
     'Sinus_T':'Sinus_Tachycardia',
     'Sinus_Tach':'Sinus_Tachycardia',
     'Sinus_Tachyc':'Sinus_Tachycardia',
     'Sinus_Tachycardi':'Sinus_Tachycardia',
     'Sinus_Tachycardia':'Sinus_Tachycardia',
     'Supravent':'Supraventricular_Tachycardia',
     'Supraventricular_Tachycardia':'Supraventricular_Tachycardia',
     'Ventricular_Fibrillation':'Ventricular_Fibrillation',
     'Ventricular_Tachycardia_(With_Pulse)':'Ventricular_Tachycardia',
     'Non_STEMI_Lateral_Ischemia':'Non_STEMI_Lateral_Ischemia'
}

pool = set(['Medical - Abdominal Pain',
            'Medical - Altered Mental Status',
            'Medical - Seizure',
            'Medical - Respiratory Distress/Asthma/COPD/Croup/Reactive Airway',
            'General - Behavioral/Patient Restraint',
            'Medical - Overdose/Poisoning - Opioid',
            'Medical - Diabetic - Hypoglycemia',
            'Medical - Chest Pain - Cardiac Suspected'])
            
FN2H = {
 '': 1,
 'aspirin': 2,
 'albuterol': 2,
 'bag valve mask ventilation': 4,
 'capnography': 2,
 'cardiac monitor': 2,
 'cpap': 4,
 'dexamethasone': 2,
 'dextrose': 4,
 'endotracheal tube':4,
 'fentanyl': 1,
 'glucagon': 3,
 'ipratropium': 2,
 'midazolam': 4,
 'morphine sulfate': 1,
 'narcan': 4,
 'nasopharyngeal airway': 4,
 'nitroglycerine': 3,
 'normal saline': 1,
 'ondansetron': 1,
 'oral glucose': 2,
 'oxygen': 3,
 'physical restraint': 3,
 'transport': 1,
 'suction the oropharynx': 3,
 'suction the nasopharynx': 3
}

FP2H = {
 '': 1,
 'aspirin': 2,
 'bag valve mask ventilation': 2,
 'cardiac monitor': 1,
 'cpap': 3,
 'dexamethasone': 2,
 'dextrose': 2,
 'midazolam': 4,
 'narcan': 2,
 'nitroglycerin': 2,
 'normal saline': 2,
 'ondansetron': 1,
 'oral glucose': 2,
 'oxygen': 1,
 'physical restraint': 2,
 'transport': 1,
 'fentanyl': 4,
 'endotracheal tube': 4
}

