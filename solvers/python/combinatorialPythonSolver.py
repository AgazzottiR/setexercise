from solvers.abstractSolver import AbstractSolver
import numpy as np
from profilers.profiler import profile  

class CombinatorialPythonSolver(AbstractSolver):
    """Computes all the possible subset of with a combinatorial approach.
    """
    def __init__(self):
        """Constructor method for a CombinatorialPythonSolver Approach.
        """
        AbstractSolver.__init__(self, "CombinatorialPythonSolver")
        self.MAX_VAL = 2**32 - 1
        self.dataSize = 0
        
    @profile
    def solve(self, data:set)->set:
        """ Solves the problem using a combinatorial approach.

        Args:
            data (set): Input

        Returns:
            list[set]: Result
        """
        self.dataSize = len(data)
        # Computes number of subsets
        cardinality = 2**len(data)
        # Computes boolean mask to index data.
        masks = self.__convert_number_to_indexes(cardinality)
        # Converts data to numpy array in order to fast index them.
        data = np.array(list(data))
        # Uses python map function to map input data to subsets. Functools are a better choice than for loops.
        res = list(map(lambda x: set(data[x].tolist()), masks))
        # Returns the result.
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
        ## Numpy Implementation to avoid slow python for loops, in spite of memory usage. ##
        
        # Build arange. vector of interger, a possible memory optimization can be performed by dynamically changing the dtype to fit the cardinality.
        masks = np.arange(cardinality, dtype=np.uint32)
        
        # Converts unsigned integers to their corresponding bit values.
        # Upacksbits returns the bit representation for a np.uint8 value or array of values.
        # Since numpy array are memory contiguous c-type like arrays we can get a memory view of it by using view function to prepare the 
        # data for the unpackbits function. i.e np.array([10], dtype=np.int32).view(np.uint8) = np.array([10,0,0,0]) -> Little endian
        # Using bit order little each bit representation is flipped making the leftmost bytes the least significative, so if the leftmost  
        # bit is 1 the 0th element of the input set is taken, what I expect from indexing. 
        # Reshaping is performed to split the mask.
        masks = np.unpackbits(masks.view(np.uint8), bitorder="little").reshape(-1,32)[:,:self.dataSize]
        
        # Converts the mask to boolean values.
        return masks == 1

        