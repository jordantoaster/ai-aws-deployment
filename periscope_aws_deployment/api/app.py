from flask import Flask, request, json
import boto3
import pickle
import joblib

BUCKET_NAME = 'periscope-aws-zappa'
MODEL_FILE_NAME = 'model.joblib'

app = Flask(__name__)
S3 = boto3.client('s3', region_name='eu-west-1')

def load_model(key):    

    with open('model.joblib', 'wb') as f:
        S3.download_fileobj(BUCKET_NAME, key, f)

    model = joblib.load('model.joblib')

    return model

@app.route('/', methods=['POST'])
def index():    
    # Parse request body for model input 
    body_dict = request.get_json(silent=True)   

    data = body_dict['data']     
    
    # Load model
    model = load_model(MODEL_FILE_NAME)

    # Make prediction 
    prediction = model.predict(data).tolist()

    # Respond with prediction result
    result = {'prediction': prediction}    
   
    return json.dumps(result)

if __name__ == '__main__':    
    # listen on all IPs 
    app.run(host='0.0.0.0', debug=True)