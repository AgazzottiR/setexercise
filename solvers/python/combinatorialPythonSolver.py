from solvers.abstractSolver import AbstractSolver
import numpy as np


class CombinatorialPythonSolver(AbstractSolver):
    """Computes all the possible subset of with a combinatorial approach.
    """
    def __init__(self):
        """Constructor method for a CombinatorialPythonSolver Approach.
        """
        AbstractSolver.__init__(self, "CombinatorialPythonSolver")
        self.MAX_VAL = 2**32
        self.dataSize = 0
    
    def solve(self, data:set)->set:
        """ Solves the problem using a combinatorial approach.

        Args:
            data (set): Input

        Returns:
            list[set]: Result
        """
        self.dataSize = len(data)
        cardinality = 2**len(data)
        masks = self.__convert_number_to_indexes(cardinality)
        data = np.array(list(data))
        res = list(map(lambda x: set(data[x].tolist()), masks))
        return res
     
    def __convert_number_to_indexes(self,cardinality):
        """ Given an array of unsigned int computes a mask that corresponds to the binary representation of the numbers themselves.

        Args:
            cardinality (int): number of element that has to be index in the result set.

        Returns:
            np.ndarray : boolean mask
        """
        if cardinality > self.MAX_VAL:
            raise ValueError("[Combinatorial Solver] Set is too big to be computed.")        
        masks = np.arange(cardinality, dtype=np.uint32)
        masks = np.unpackbits(masks.view(np.uint8), bitorder="little").reshape(-1,32)[:,:self.dataSize]
        return masks == 1

        