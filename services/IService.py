from abc import ABC, abstractmethod



class IService(ABC):
    """ Interface that a service can implement
    """
    @abstractmethod
    def run(self, data):
        """ Executes the service task according to the input data.
        """
        pass