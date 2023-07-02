import unittest
import os
import pathlib
from services.subsetCalculatorService import SubSetCalculatorService
from unittests.utils import result_verifier
import random
import json

class SubSetCalculatorServiceTest(unittest.TestCase):
    """Test cases for the SubSetCalculatorService
    """
    def setUp(self) -> None:
        """ Loads A random test case
        """
        folderPaths = os.path.join(str(pathlib.Path(__file__).parent.parent.parent),"data", "testConfigurations")
        path = random.choice([os.path.join(folderPaths,a) for a in os.listdir(folderPaths) if not a.__contains__("TEMPLATE")])
        print("Chosen case -> ", path)
        self.solutionPath = os.path.join(path, "solution.json")
        self.solutionPath = self.solutionPath if os.path.exists(self.solutionPath) else None
        self.path = os.path.join(path, "serviceConf.json")
        return super().setUp()
    
    def test_0_compute_a_random_configuration(self):
        service = SubSetCalculatorService(self.path)
        retval = service.run()
        if self.solutionPath is not None:
            with open(self.solutionPath, "r") as f:
                data = json.load(f)
            result = data["solution"]           
            print("Return Value ", retval)
            self.assertTrue(result_verifier(retval, result))
        else:
            print("Return Value ", retval)
            self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()