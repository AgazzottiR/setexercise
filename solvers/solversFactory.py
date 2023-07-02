from solvers.python.combinatorialPythonSolver import CombinatorialPythonSolver
from solvers.python.recursivePythonSolver import RecursivePythonSolver


class SolverFactory:
    @staticmethod
    def get_solver(solverName):
        if solverName == "combinatory_python":
            return CombinatorialPythonSolver()
        elif solverName == "recursive_solver":
            return RecursivePythonSolver()
        else:
            raise NotImplementedError("[Solver Factory] Solver not found.")


