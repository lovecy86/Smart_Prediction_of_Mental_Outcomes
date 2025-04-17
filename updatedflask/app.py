from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model with joblib
model = joblib.load('ten_feature_model.pkl')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        user_input = {
            'Country': request.form['Where_do_you_live'],
            'care_options': request.form['care_options'],
            'family_history': request.form['family_history'],
            'mental_health_interview': request.form['mental_health_interview'],
            'self_employed': request.form['self_employed'],
            'Gender': request.form['Gender'],
            'Days_Indoors': request.form['Days_Indoors'],
            'Occupation': request.form['Occupation'],
            'Social_Weakness': request.form['Social_Weakness'],
            'Work_Interest': request.form['Work_Interest']
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([user_input])
        
        # Predict (no preprocessing needed, CatBoost handles categorical features)
        prediction = model.predict(input_df)[0]
        
        # Return JSON for AJAX
        return jsonify({'prediction': str(prediction)})
    
    except Exception as e:
        # Return JSON error for AJAX
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
# if __name__ == '__main__':
#     app.run(host='0.0.0.0' , port=8080)