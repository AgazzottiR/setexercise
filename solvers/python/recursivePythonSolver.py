from solvers.abstractSolver import AbstractSolver


class RecursivePythonSolver(AbstractSolver):
    def __init__(self):
        AbstractSolver.__init__(self, "RecursivePython")

    def solve(self, param:str) -> str:
        pass
    

    def _recursive_call(self, value:set):
        pass