from solvers.abstractSolver import AbstractSolver


class RecursivePythonSolver(AbstractSolver):
    def __init__(self):
        AbstractSolver.__init__(self, "RecursivePython")

    def solve(self, data:set) -> list:
        return list(map(lambda x : set(x), self.__recursive_call(list(data),0)))
    
    def __recursive_call(self, sourceSet:list, index:int) -> list:
        allSubSets = []
        if(len(sourceSet) == index):
            allSubSets.append([])
        else:
            allSubSets = self.__recursive_call(sourceSet,index+1)
            item = sourceSet[index]
            moreSubSet = []
            for subSet in allSubSets:
                newSubSets = []
                newSubSets.extend([*subSet, item])
                moreSubSet.append(newSubSets)
            allSubSets.extend(moreSubSet)

        return allSubSets
