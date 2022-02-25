import pickle
import numpy as  np
import pandas as pd


class Model:
    
    def __init__(self) -> None: 
        

        self.engine = pickle.load(open('model.pkl','rb')) 

        
    def predict(self, data) -> dict: 
        
        # convert data into dataframe
        data.update((x, [y]) for x, y in data.items())
        data_df = pd.DataFrame.from_dict(data)
        # predictions
        result = self.engine.predict(data_df)
        
        # send back to browser
        output = {'results': int(result[0])}
        
        return output 