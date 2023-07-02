import unittest
import os
from dataAdapters.jsonAdapter import JsonAdapter

class JsonAdapterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.filename = "data/testConfigurations/case2/data.json"
        return super().setUp()

    def test_0_convert_to(self):
        ja = JsonAdapter()
        print(ja.convert(self.filename))




if __name__ == "__main__":
    unittest.main()


