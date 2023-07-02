from services.abstractService import AbstractService


class SubSetCalculatorService(AbstractService):
    """ Service that computes all the subsets of a set. 
    """
    def __init__(self, configurationPath:str):
        """ Constructor.
        Args:
            configurationPath (str): configuration Path.
        """
        self.configurationPath = configurationPath
    
    def run(self, data):
        """ Computes all the possible subsets of the data.

        Args:
            data (set): Input set.
        """
        pass