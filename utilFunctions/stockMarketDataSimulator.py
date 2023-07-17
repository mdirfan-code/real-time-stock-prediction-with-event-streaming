import pandas as pd

class stockDataSimulator():

    def __init__(self):
        pass
    
    def get_data(self,Index='HSI'):
        '''
        This generator function returns the stocks metrics data.
        '''
        dataFrame = pd.read_csv('static/indexProcessed.csv')
        dataFrame = dataFrame[dataFrame['Index']==Index]
        for data in dataFrame.iterrows():
            yield dict(data[1])
        

        


