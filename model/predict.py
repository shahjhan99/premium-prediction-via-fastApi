
import pickle
import pandas as pd
from schema.user_input import UserInput
#from model.predict import predict_output, model, MODEL_VERSION

# open the model file and load the model
with open('model/insurance_model.pkl', 'rb') as f:
    model = pickle.load(f)


MODEL_VERSION = '1.0.0'

class_labels =model.classes_.tolist()

def predict_output(user_input: dict):
  
   df = pd.DataFrame([user_input])
        
   predicted_class=output = model.predict(df)[0]
   probablities = model.predict_proba(df)[0]
   confidence = max(probablities)

   class_probs = dict(zip(class_labels, map(lambda p:round(p,4), probablities)))
   
   return {
       "predicted_catagory": predicted_class,
       "confidence": confidence,
       "class_probablities":class_probs
   }
   
