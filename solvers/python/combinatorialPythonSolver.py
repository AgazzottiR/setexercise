from solvers.abstractSolver import AbstractSolver
import numpy as np


class CombinatorialPythonSolver(AbstractSolver):
    """Computes all the possible subset of with a combinatorial approach.
    """
    def __init__(self):
        """Constructor method for a CombinatorialPythonSolver Approach.
        """
        AbstractSolver.__init__(self, "CombinatorialPythonSolver")
    
    def solve(self, data:set)->set:
        """ Solves the problem using a combinatorial approach.

        Args:
            data (set): Input

        Returns:
            set: Result
        """
        cardinality = 2**len(data)
        masks = self.__convert_number_to_indexes(cardinality)
        data = np.array(list(data))
        res = list(map(lambda x: data[x].tolist(), masks))
        return res
     
    def __convert_number_to_indexes(self,cardinality):
        masks = np.arange(cardinality, dtype=np.uint32)
        masks = np.unpackbits(masks.view(np.uint8), bitorder="little").reshape(-1,32)[:,:int(np.log2(cardinality))]
        return masks == 1

        