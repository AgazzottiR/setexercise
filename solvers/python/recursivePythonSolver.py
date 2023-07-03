from solvers.abstractSolver import AbstractSolver
from profilers.profiler import profile  

class RecursivePythonSolver(AbstractSolver):
    """ Solves the subset problem in a recursive way.
    """
    def __init__(self):
        AbstractSolver.__init__(self, "RecursivePython")

    @profile
    def solve(self, data:set) -> list:
        """ Computes the solution

        Args:
            data (set): Input Data

        Returns:
            list: List of subsets.
        """
        return list(map(lambda x : set(x), self.__recursive_call(list(data),0)))
    
    def __recursive_call(self, sourceSet:list, index:int) -> list:
        """ Python function that computes the subsets recursively.
        Args:
            sourceSet (list): data
            index (int): index of the input data the function is computing

        Returns:
            list: Subsets.
        """
        # List to store the result.
        allSubSets = []
        # Statement that stops the recursion.
        if(len(sourceSet) == index):
            # Adds the empty set.
            allSubSets.append([])
        else:
            # Unrolls the array recursively. [Can be done also with a loop] 
            allSubSets = self.__recursive_call(sourceSet,index+1)
            # Get the element to process
            item = sourceSet[index]
            # Variable to store the subsets that has to be added
            moreSubSet = []
            for subSet in allSubSets:
                # Adds set to the new set to be computed
                moreSubSet.append([*subSet, item])
            # Adds the computed sets at the existing ones.
            allSubSets.extend(moreSubSet)
        # Returns the results.
        return allSubSets
