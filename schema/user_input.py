from pydantic import BaseModel, Field,computed_field
from typing import Literal, Annotated,Optional
from config.city_tier import rank_1, rank_2, rank_3




# pydantic model to validate the User Input data

class UserInput(BaseModel):
    age:Annotated[int, Field(..., gt=0, lt=120, description="Age of User")]
    weight:Annotated[float,Field(..., gt=0, description="Weight of  user")]
    height:Annotated[float, Field(..., gt=0, lt= 2.5, description="Height of user")]
    income_lpa:Annotated[float,Field(..., gt= 0, description="Annual Salary of user")]
    smoker:Annotated[bool, Field(..., description="Is user a Smoker")]
    city:Annotated[Literal[ 'Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Faisalabad', 'Multan', 'Peshawar',
                            'Quetta', 'Sialkot', 'Gujranwala', 'Hyderabad', 'Abbottabad', 'Bahawalpur', 'Sukkur',
                            'Sargodha', 'Larkana', 'Mirpur', 'Mardan', 'Dera Ghazi Khan', 'Rahim Yar Khan'], Field(...,description="City the user belongs to")]
    occupation:Annotated[Literal['unemployed', 'business_owner', 'freelancer', 'private_job',
                             'retired', 'student', 'government_job'], Field(..., description="Occupatuion of user")]   


    @computed_field 
    @property
    def bmi(self)-> float:
        return self.weight/(self.height**2)
    
    @computed_field 
    @property
    def age_gropu(self)-> str:
        if  self.age <= 25:
            return "middle_aged"
        elif self.age >= 25 and self.age <= 45:
            return "young_aged"
        elif self.age > 45:
            return "old_aged"
        else:
            return None
        

    @computed_field
    @property
    def lifestyle_risk (self)->str:
        
        if self.smoker == True:
            if self.bmi >= 30:
                 return 'High'
            elif self.bmi >= 18.5:
                 return 'Medium'
            else:
                 return 'Medium' if self.age_gropu == 'young_aged' else 'High'
        
        else:  
                if self.age_gropu == 'old_aged' and self.bmi >= 30:
                    return 'High'
                elif self.age_gropu == 'young_aged' and self.bmi < 25:
                    return 'Low'
                elif self.age_gropu == 'middle_aged' and self.bmi >= 25:
                    return 'Medium'
                else:
                    return 'Low' 
                

    @computed_field
    @property
    def city_tier(self)-> int:        
            if self.city in rank_1:
                return 1
            elif self.city in rank_2:
                return 2
            elif self.city in rank_3:
                return 3
            else:
                return None