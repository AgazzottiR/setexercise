from abc import ABC,abstractmethod


class AbstractSolver(ABC):
    """Abstract Solver is the abstraction on top of 
       which all the solvers of our problem should rely on.
    """
    @abstractmethod
    def __init__(self, solverType: str):
        """Constructor method for solver class

        Args:
            solverName (string): The name of the solver. 
        """
        self.solverType = solverType

    @abstractmethod
    def solve(self,params: set) -> set:
        """
        Solve method. Takes in a set of values and produces all the sub sets.

        Args:
            params(set): The values provided as input to the problem.

        returns:
            results(set): Result values        
        """ 
