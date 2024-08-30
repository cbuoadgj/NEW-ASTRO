from pydantic import BaseModel

class starproperties(BaseModel):
    temperature : float
    luminosity : float
    radius : float
    abs_mag : float