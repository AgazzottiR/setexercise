from dataAdapters.abstractAdapter import AbstractAdapter
import os 
import json
from collections.abc import Iterable

class JsonAdapter(AbstractAdapter):
    """ Json Adapter. Class to deal with json files as input.
    """
    def __init__(self):
        AbstractAdapter.__init__(self,"JsonAdapter")
    
    def convert(self, data) -> set:
        """
        Converts json loaded data to a set.
        
        Args:
            data(dict): input data, loaded from a json object
        
        Return:
            Set of data.
        """
        if isinstance(data,str):
            return self.load_from_json_file(data)
        

        if not isinstance(data["data"], Iterable):
            raise ValueError("[Json Adapter] Input data should be at least iterable")
        
        previousLength = len(data["data"])

        if previousLength != 0:
            if not isinstance(data["data"][0],int):
                raise ValueError("[Json Adapter] Input data type should be integers")

        setData = set(data["data"])

        if previousLength != len(setData):
            raise ValueError("[Json Adapter] Input data are not unique.")
        
        return setData
        


    def load_from_json_file(self, dataPath:str):
        """ 
        Loads data from a json file. Expecting a data key inside the json file.

        Args:
            dataPath (str): path to the json file.  
        """
        if not os.path.exists(dataPath):
            raise FileNotFoundError(f"[JsonAdapter] The input path  {dataPath} is not existing.")
        
        data = None
        with open(dataPath, "r") as f:
            data = json.load(f)

        if not isinstance(data, dict) or not "data" in data:
            raise ValueError("[Json Adapter] The input path is not correctly formatted.")
    

        return self.convert(data)
        
        
                  
        
