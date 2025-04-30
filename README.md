# **Smart Prediction of Mental Health**
A model to predict mental health treatment needs based on lifestyle, personal history, and social factors, enabling early intervention for healthcare professionals.

## **Table of Contents**
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Project Steps](#project-steps)
- [Model Development](#model-development)
- [Technologies Used](#technologies-used)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Contributing](#contributing)
- [Next Steps](#next-steps)
- [License](#license)
  
## **Problem Statement**:
The Smart Prediction of Mental Health project addresses the challenge of late detection of mental health issues, which delays critical interventions and strains healthcare resources. By developing a model, the project predicts the likelihood of individuals needing mental health treatment based on factors such as lifestyle, occupation, and family history. The goal is to enable psychologists, psychiatrists, general practitioners, and mental health counselors to identify at-risk individuals early, prioritize interventions, allocate resources efficiently, and improve patient outcomes through proactive support.

---

## **Dataset**

- **Source**: [Mental Health Dataset](https://www.kaggle.com/datasets/divaniazzahra/mental-health-dataset)
- **Sample Size**: 292374 records
- **Target Variable**: treatment (binary: needs treatment or not).
- **Features**:
  - Timestamp 
  - Gender
  - Country
  - Occupation
  - Self-employed status
  - Family History
  - Growing Stress
  - Changes Habits
  - Mood Swings
  - Coping Struggles
  - Work Interest
  - Social Weakness
  - Days indoors
  - Mental health history
  - Care Options
  - Mental Health Interview
    
---

## **Project Steps**
**1. Data Cleaning**
- Dropped Timestamp due to incomplete monthly data.
- Removed duplicates and null values.
- Grouped rare countries (<1,000 counts) into ‘Other’.
- Reduced dataset to 286808 rows after preprocessing.

![cleaned dataset](images/cleaned_dataset.png)

**2. Exploratory Data Analysis** 
- Visualized balanced treatment distribution using count plots.
  
![treatment Distribution](images/treatment_distribution.png)

- Analyzed categorical features’ impact on treatment with count plots and hue.
- Conducted Cramér’s V correlation analysis to identify feature relationships.

**3. Data Preprocessing**
- Encoded categorical variables using OneHotEncoder for Logistic Regression and MLP.
- Used LabelEncoder for target variable (Yes/No).

**4. Modeling**
- Trained Logistic Regression, MLP, and CatBoost models.
- Split data 80/20 (train/test).
- Best accuracy: 78.59% (CatBoost with 10 features).

**5. Optimization**
- Tuned CatBoost hyperparameters (iterations, depth, learning rate)
- Reduced dimensionality to 10 features and 6 features without accuracy loss.
- Saved models using pickle for deployment.

**6. Deployment**
Deployed the CatBoost model (10 features) on AWS EC2 via a Flask web app for real-time predictions.

## **Model Development**
### **Models Used**
  **1. CatBoost Classifier (Selected):** 
    - The reason for initially selecting this model is that it is a gradient boosting machine learning library designed to handle categorical features efficiently.The dataset includes only categorcal features. It uses a combination of ordered boosting, symmetric trees, and a novel approach to encode categorical variables, reducing the need for extensive preprocessing.
    - Achieved 78.59% accuracy with 15 features (iterations=500, depth=6, learning_rate=0.1).

![catboost](images/catboost.png)

  **2. Logistic Regression:**
    - Logistic Regression is a baseline model that gave an accuracy of 71.3%.
    
![logistic](images/logistic.png)
    

  **3. MLP (Multi-Layer Perceptron):**
    - A neural network model for capturing deep, complex relationships in the data to improve prediction accuracy.
    - This model gave an accuracy of 78.32%

![mlp](images/mlp.png)

### **Analysis**
  Among all models catboost model gave a better accuracy (78.59%). Logistic regression model gave very low accuracy. MLP gave almost same accuracy.


## **Feature Importance on Catboost Model**: 
  - This was done to determine the features that had more effect on the target.
  - Therefore, modeling with top 10 and top 6 features were done to determine if feature reduction would affect the accuracy in any way.

![feature_importance](images/feature_importance.png)

---

## **Key Insights**
- Final model used for deployment is Catboost model with top 10 features - Country, care_options, mental_health_interview, family_history, self_employed, Gender, Growing_Stress, Mental_Health_History, Mood_Swings, Occupation' significantly influence treatment needs.
- This model enables early detection for proactive intervention.

## **Technologies Used**
  - Data Processing: Python, pandas, numpy, PySpark
  - Visualization: matplotlib, seaborn
  - Machine Learning: scikit-learn, catboost, logistic regression, MLPclassifer
  - Web Development: Flask
  - Deployment: AWS EC2
  - Tools: Jupyter, Google Colab, findspark, pickle

## **Repository Structure**

Smart_Prediction_of_Mental_Health

├── images  # Visualizations (graphs, confusion matrices)

├── flask_and_deployment/     # Flask app and deployment files

│   ├── app.py

│   └── requirements.txt

├── Mental_Health_Prediction_in_colab.ipynb  # Modeling notebook

├── README.md

└── LICENSE

## **Installation**
1. Clone the repository
git clone https://github.com/lovecy86/Smart_Prediction_of_Mental_Health.git
cd Smart_Prediction_of_Mental_Outcomes
2. Install dependencies
pip install -r flask_and_deployment/requirements.txt
3. Run the Flask app
python flask_and_deployment/app.py
4. Access at http://127.0.0.1:5000/

## **Prerequisites**
- Python 3.8+
- AWS account (for EC2 deployment)

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (git checkout -b feature-branch).
3. Commit changes (git commit -m "Add feature").
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.

## **Next Steps**
1. Integrate real-time health data from wearable devices (e.g., Fitbit, Apple Watch).
2. Expand dataset with additional features or larger sample size.
3. Enhance Flask app for improved user interaction.

## **License**
This project is licensed under the MIT License - see the LICENSE file for details.

## **AWS Deployment**
http://ec2-35-182-98-44.ca-central-1.compute.amazonaws.com:8080/


