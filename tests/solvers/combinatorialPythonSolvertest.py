import unittest 
from solvers.python.combinatorialPythonSolver import CombinatorialPythonSolver
import numpy as np

class CombinatorialPythonSolverTest(unittest.TestCase):
    def setUp(self) -> None:
        
        return super().setUp()


    def test_0_solve_all_subset(self):
        data = {0,-1,2,3}
        solver = CombinatorialPythonSolver()    
        ret = solver.solve(data) 
        print(ret)
        print(len(ret))   
        



if __name__ == "__main__":
    unittest.main()