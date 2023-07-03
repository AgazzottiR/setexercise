import unittest
from solvers.python.recursivePythonSolver import RecursivePythonSolver
from unittests.utils import result_verifier


class RecursivePythonSolverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {1,2,3} 
        self.solution = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        return super().setUp()

    def test_0_solve_all_subset(self):
        solver = RecursivePythonSolver()    
        print(f"Input -> {self.data}")
        ret = solver.solve(self.data) 
        print(f"Results[{len(ret)}]-> {ret}")
        self.assertTrue(result_verifier(self.solution,ret))

    def test_1_empty_set(self):
        solver = RecursivePythonSolver()    
        print(f"Input -> {{}}")
        ret = solver.solve({}) 
        print(f"Results[{len(ret)}]-> {ret}")
        self.assertTrue(len(ret) == 1 and len(ret[0]) == 0)


if __name__ == "__main__":
    unittest.main()