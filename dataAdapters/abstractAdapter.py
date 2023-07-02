from abc import ABC, abstractmethod


class AbstractAdapter(ABC):
    """Abstract class for data adapting.
       The purpose of these hierarchy of classes is to convert generic input data to 
       a set, target format for the solvers as input for the solvers.
    """
    @abstractmethod
    def __init__(self, adapterType:str):
        """Abstract constructor of adapter class.
        """
        self.adapterType = adapterType
    

    @abstractmethod
    def convert(self,data)->set:
        """
           Method that should be called to convert data from input to output.
        Args:
            data : input data to convert. 

        Returns:
            set: valid set to use as input data
        """
        pass