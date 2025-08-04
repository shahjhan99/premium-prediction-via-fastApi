from pydantic import BaseModel, Field
from typing import Dict


class prediction_response(BaseModel):
    predicted_catagory :str = Field(
        ...,
        description = "The Predicted Insurance Premium", 
        example = "High"
        )
    confidence :float = Field(
        ...,
        description = "Model is confidence score for the predicted class (range: 0 - 1 )", 
        example = "High"
        )
    class_probablities :Dict[str, float] = Field(
        ...,
        description = "Probablities Distribution across all possible classes", 
        example = {"Low":0.01 ,"Medium ": 0.15  ,"High":0.84   }  )
