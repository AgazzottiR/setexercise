import unittest
import os
from dataAdapters.jsonAdapter import JsonAdapter

class JsonAdapterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.filename = "data/testConfigurations/case2/data.json"
        return super().setUp()

    def test_0_load_data_from_test_case(self):
        ja = JsonAdapter()
        print(ja.load_from_json_file(self.filename))




if __name__ == "__main__":
    unittest.main()


