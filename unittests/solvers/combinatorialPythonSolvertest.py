import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from solvers.python.combinatorialPythonSolver import CombinatorialPythonSolver
import numpy as np
from unittests.utils import result_verifier

class CombinatorialPythonSolverTest(unittest.TestCase):

    def test_0_solve_all_subset(self):
        data = {1,2,3}
        solution = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        solver = CombinatorialPythonSolver()     
        print(f"Input -> {data}")
        ret = solver.solve(data) 
        print(f"Results[{len(ret)}]-> {ret}")
        self.assertTrue(result_verifier(solution,ret))

    def test_1_empty_set(self):
        solver = CombinatorialPythonSolver()    
        print(f"Input -> {{}}")
        ret = solver.solve({}) 
        print(f"Results[{len(ret)}]-> {ret}")
        self.assertTrue(len(ret) == 1 and len(ret[0]) == 0)

    def test_2_large_set_test(self):
        data = {-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        solutionLength = 2**len(data)
        solver = CombinatorialPythonSolver()     
        print(f"Input -> {data}")
        ret = solver.solve(data)
        print(f"Result[{len(ret)}]")
        self.assertEqual(len(ret),solutionLength)
        
if __name__ == "__main__":
    unittest.main()