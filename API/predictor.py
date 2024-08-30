import pickle
import warnings
ignore_warnings = False

# Load the trained model
def load_model(model_path):
    with open(model_path, 'rb') as f:
        return pickle.load(f)

# Make predictions based on the loaded model
def make_predictions(model,input_features):
    predict_class = model.predict(input_features)[0]
    probability = model.predict_proba(input_features)[0]
    classes = model.classes_
    return predict_class, probability, classes
