from dataAdapters.abstractAdapter import AbstractAdapter



class JsonAdapter(AbstractAdapter):
    """ Json Adapter. Class to deal with json files as input.
    """
    def __init__(self):
        AbstractAdapter.__init__("JsonAdapter")
    
    def convert(self, data:dict) -> set:
        pass

    def load_from_json_file(self, dataPath:str):
        pass
