from services.abstractService import AbstractService
from solvers.solversFactory import SolverFactory
from dataAdapters.adapterFactory import AdapterFactory

class SubSetCalculatorService(AbstractService):
    """ Service that computes all the subsets of a set. 
    """
    def __init__(self, configurationPath:str):
        """ Constructor.
        Args:
            configurationPath (str): configuration Path.
        """
        AbstractService.__init__(self, configurationPath)
        self.solver = SolverFactory.get_solver(self.configuration["solver"])
        self.dataAdapter = AdapterFactory.get_adapter(self.configuration["input_data_type"])

    def run(self):
        """ Computes all the possible subsets of the data.
        """
        data = self.dataAdapter.convert(self.configuration["input_data_path"])
        return self.solver.solve(data)
        