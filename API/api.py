from fastapi import FastAPI
from star_data import starproperties
import warnings 
warnings.filterwarnings("ignore")

# Import necessary libraries for model loading and prediction
import numpy as np
import uvicorn
from predictor import load_model, make_predictions

app=FastAPI()

model=load_model('model.pkl')

@app.get('/')
def index_root():
    return {"message":"HEALTH IS COOL"}

@app.post('/predict')

def predict_star_type(sp: starproperties):
    input_features =[[sp.temperature, sp.luminosity, sp.radius, sp.abs_mag]]
    make_predictions(model,input_features)
    predicted_class,probs,classes=make_predictions(model,input_features)
    return {
        'Predicted_Probabilities':dict(zip(classes,probs)),
         'Predicted_Class': predicted_class,
         'Confidence_score':str(round(np.max(probs),3)*100)+'%'
    }

# Run the FastAPI app on a local server
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
