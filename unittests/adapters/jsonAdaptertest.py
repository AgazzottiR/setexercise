import unittest
import os
from dataAdapters.jsonAdapter import JsonAdapter
from unittests.utils import result_verifier


class JsonAdapterTest(unittest.TestCase):
    """ Test Cases for the json adapter.
    """
    def setUp(self) -> None:
        self.filename = "data/testConfigurations/case0/data.json"
        return super().setUp()

    def test_0_convert_to(self):
        ja = JsonAdapter()
        data = ja.convert(self.filename)
        self.assertTrue(data == {1,2,3})




if __name__ == "__main__":
    unittest.main()


