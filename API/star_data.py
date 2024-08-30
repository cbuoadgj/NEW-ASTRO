from pydantic import BaseModel, Field

class starproperties(BaseModel):
    temperature: float = Field(..., description="Star temperature in Kelvin")
    luminosity: float = Field(..., description="Star luminosity in solar units")
    radius: float = Field(..., description="Star radius in solar units")
    abs_mag: float = Field(..., description="Absolute Magnitude of the")

pred_prob_example={
    "prediction": "Red Giant",
    "probability": 0.85
    }

class Prediction(BaseModel):
    Predicted_Probabilities: str = Field(description="Predicted probabilities")
    Predicted_class: str = Field(description="Predicted star type")
    Confidence_score: str = Field(description="Star properties")