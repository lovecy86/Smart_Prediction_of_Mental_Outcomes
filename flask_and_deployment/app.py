from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model with joblib
model = joblib.load('ten_features_model_opt1.pkl')

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
            'mental_health_interview': request.form['mental_health_interview'],
            'family_history': request.form['family_history'],
            'self_employed': request.form['self_employed'],
            'Gender': request.form['Gender'],
            'Growing_Stress': request.form['Growing_Stress'],
            'Mental_Health_History': request.form['Mental_Health_History'],
            'Mood_Swings': request.form['Mood_Swings'],
            'Occupation': request.form['Occupation']
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

#if __name__ == '__main__':
    #app.run(debug=True)

# Use the below code when deploying in cloud and uncomment the abouve line
if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=8080)