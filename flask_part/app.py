from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model
try:
    model = joblib.load('model.pkl')
except FileNotFoundError:
    print("Error: model.pkl not found in project directory")
    exit(1)

# Define feature options
feature_options = {
    'Gender': ['Male', 'Female'],
    'Country': ['United States', 'United Kingdom', 'Canada', 'Other', 'Australia', 
                'Netherlands', 'Ireland', 'Germany', 'Sweden', 'India', 'France', 
                'Brazil', 'South Africa', 'New Zealand', 'Switzerland', 'Israel', 'Italy'],
    'Occupation': ['Corporate', 'Student', 'Business', 'Housewife', 'Others'],
    'self_employed': ['Yes', 'No'],
    'family_history': ['Yes', 'No'],
    'Growing_Stress': ['Yes', 'No', 'Maybe'],
    'Mental_Health_History': ['Yes', 'No', 'Maybe'],
    'Coping_Struggles': ['Yes', 'No'],
    'mental_health_interview': ['Yes', 'No', 'Maybe'],
    'care_options': ['Yes', 'No', 'Not sure']
}

@app.route('/')
def home():
    return render_template('index.html', feature_options=feature_options, prediction=None, user_input=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs
        user_input = {
            'Gender': request.form['Gender'],
            'Country': request.form['Country'],
            'Occupation': request.form['Occupation'],
            'self_employed': request.form['self_employed'],
            'family_history': request.form['family_history'],
            'Growing_Stress': request.form['Growing_Stress'],
            'Mental_Health_History': request.form['Mental_Health_History'],
            'Coping_Struggles': request.form['Coping_Struggles'],
            'mental_health_interview': request.form['mental_health_interview'],
            'care_options': request.form['care_options']
        }
        
        # Create DataFrame for prediction
        input_df = pd.DataFrame([user_input])
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        
        # Render template with prediction
        return render_template('index.html', feature_options=feature_options, 
                             prediction=prediction, user_input=user_input)
    
    except Exception as e:
        error_message = f"Error during prediction: {str(e)}"
        return render_template('index.html', feature_options=feature_options, 
                             error=error_message, user_input=None)

if __name__ == '__main__':
    app.run(debug=True)