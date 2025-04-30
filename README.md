# **Smart Prediction of Mental Health: Sentiment Analysis Model**
A sentiment analysis model to predict mental health treatment needs based on lifestyle, personal history, and social factors, enabling early intervention for healthcare professionals.

[Modeling Code](https://github.com/lovecy86/Smart_Prediction_of_Mental_Outcomes/blob/main/Mental_Health_Prediction_in_colab.ipynb)

[Flask and Deployment](https://github.com/lovecy86/Smart_Prediction_of_Mental_Outcomes/tree/main/flask_and_deployment)

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
- [Authors](#authors)
- [License](#license)
  
## **Problem Statement**:
The Smart Prediction of Mental Health project addresses the challenge of late detection of mental health issues, which delays critical interventions and strains healthcare resources. By developing a sentiment analysis model, the project predicts the likelihood of individuals needing mental health treatment based on factors such as lifestyle, occupation, and family history. The goal is to enable psychologists, psychiatrists, general practitioners, and mental health counselors to identify at-risk individuals early, prioritize interventions, allocate resources efficiently, and improve patient outcomes through proactive support.

---

## **Dataset**

- **Source**: Kaggle Mental Health Dataset- [Mental Health Dataset](https://www.kaggle.com/datasets/divaniazzahra/mental-health-dataset)
- **Sample Size**: 292000 records
- **Target Variable**: treatment (binary: needs treatment or not).
- **Key Features**:
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
- Best accuracy: 78.63% (CatBoost with 10 features).

**5. Optimization**
- Tuned CatBoost hyperparameters (iterations, depth, learning rate)
- Reduced dimensionality to 10 features and 6 features without accuracy loss.
- Saved models using pickle for deployment.

**6. Deployment**
Deployed the CatBoost model (10 features) on AWS EC2 via a Flask web app for real-time predictions.

## **Model Development**
### **Models Used**
  **CatBoost Classifier (Selected):** 
    - The reason for initially selecting this model is that it is a gradient boosting machine learning library designed to handle categorical features efficiently.The dataset includes only categorcal features. It uses a combination of ordered boosting, symmetric trees, and a novel approach to encode categorical variables, reducing the need for extensive preprocessing.
    - Achieved 78.61% accuracy with 15 features (iterations=500, depth=6, learning_rate=0.1).

   ![catboost](images/catboost.png)

  **Logistic Regression:**
    - Logistic Regression is a baseline model that gave an accuracy of 71%.
    
  ![logistic](images/logistic.png)
    

  **MLP (Multi-Layer Perceptron):**
    - A neural network model for capturing deep, complex relationships in the data to improve prediction accuracy.
    - This model gave an accuracy of 78.58%

  ![mlp](images/mlp.png)

### **Analysis**
  Among all models catboost model gave a better accuracy (78.61%). Logistic regression model gave very low accuracy. MLP gave almost same accuracy.


## **Feature Importance on Catboost Model**: This was done to determine the features that had more effect on the target. 

![feature_importance](images/feature_importance.png)

### **Model Evaluation**
- **Accuracy**: Achieved **78.63%** accuracy using **CatBoost**.
- **Precision, Recall, and F1-Score**: Evaluated the model’s ability to predict mental health outcomes correctly, with a focus on minimizing false positives and false negatives.
- **Key Insights**: country, occupation, and family history were found to be significant predictors for mental health treatment needs.

![final_model](images/final_model.png)
![confusion_matrix](images/confusion_matrix.png)

### **Tuning and Optimization**
- **Hyperparameter Tuning**: Used **feature selection** and **tuning** to optimize model hyperparameters and enhance prediction accuracy.


---

## **Deployment**

### **Flask Web Application**
- Developed a **Flask web application** that allows healthcare providers and employers to input real-time data (e.g., occupation, family history) and receive predictions on mental health outcomes.
- **Flask** was chosen for its simplicity and ease of deployment, creating an interactive interface for end-users.

### **AWS EC2 Hosting**
- The Flask application was deployed on **AWS EC2** to ensure scalability and reliable access.
  
#### **EC2 Deployment Steps**:
1. **Create EC2 Instance**: Launch a new EC2 instance with Amazon Linux as the operating system.
2. **SSH Access**: Connect to the EC2 instance using SSH:
   ```bash
   ssh -i <your-key-pair.pem> ubuntu@<ec2-public-ip>
   ```
3. **Install Dependencies**:
   - Install Python and libraries:
     ```bash
     sudo apt update
     sudo apt install python3-pip
     pip3 install -r requirements.txt
     ```
4. **Transfer and Deploy**:
   - Upload your Flask app to the EC2 instance (using SCP or Git).
   - Start the Flask app:
     ```bash
     python3 app.py
     ```
5. **Configure Security**: Ensure the EC2 security group allows traffic on ports 80 (HTTP) or 5000 (Flask default).
6. **Access Application**: The web application will be accessible via the public IP of the EC2 instance.

---

## **Key Results**

- **Accuracy**: Achieved **78.63%** accuracy using **CatBoost**. 
- **Insights**: Key predictors such as **family history**, **occupation**, and **country** significantly influenced the prediction of mental health treatment needs.
- **Impact**: The model enables **early detection** and supports **proactive intervention** in mental health management.

---

## **Future Work**

- **Integration with Wearable Data**:  
  - Incorporate real-time health data from wearable devices (e.g., Fitbit, Apple Watch) to enhance the model’s predictive accuracy. This would allow for continuous monitoring of individuals' physical and mental health, providing more personalized and timely predictions for mental health interventions.

---

## **Installation**

To run this project locally, clone the repository and install the required dependencies:

```bash
git clone <repository_url>
cd <repository_folder>
pip install -r requirements.txt
```

### **Run the Application**
To start the Flask application, run:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/`.

---

## **Authors**
- **Dhruvi Yadav**
- **Bansri Patel**
- **Lovecy Thomas**

---
