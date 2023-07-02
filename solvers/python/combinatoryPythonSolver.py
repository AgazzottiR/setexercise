from solvers.abstractSolver import AbstractSolver



class CombinatorialPythonSolver(AbstractSolver):
    """Computes all the possible subset of with a combinatorial approach.
    """
    def __init__(self):
        """Constructor method for a CombinatorialPythonSolver Approach.
        """
        AbstractSolver.__init__(self, "CombinatorialPythonSolver")
    
    def solve(self, params:str)->str:
        pass