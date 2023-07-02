import unittest 
from solvers.python.combinatorialPythonSolver import CombinatorialPythonSolver

class CombinatorialPythonSolverTest(unittest.TestCase):
    def test_0_solve_all_subset(self):
        data = {1,2,3}
        solver = CombinatorialPythonSolver()    
        ret = solver.solve(data)    
        



if __name__ == "__main__":
    unittest.main()