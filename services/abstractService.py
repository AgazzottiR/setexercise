from abc import ABC, abstractmethod
import json


class AbstractService(ABC):
    """ Interface that a service can implement
    """
    def __init__(self, configurationPath):
        self.configurationAttributes = ['solver', 'input_data_type', 'input_data_path']
        self.configurationPath = configurationPath
        self.configuration = None
        self.load_configuration()

    def load_configuration(self):
        with open(self.configurationPath, 'r') as f:
            self.configuration = json.load(f)

        assert all([att in self.configuration for att in self.configurationAttributes])
        

    @abstractmethod
    def run(self, data):
        """ Executes the service task according to the input data.
        """
        pass

