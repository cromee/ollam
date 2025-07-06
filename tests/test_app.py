import json
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import app

class QueryModelTest(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_query_model(self, mock_urlopen):
        fake_response = MagicMock()
        fake_response.read.return_value = json.dumps({"message": {"content": "hi"}}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = fake_response

        result = app.query_model("hello", "context", model="testmodel")
        self.assertEqual(result, "hi")

if __name__ == '__main__':
    unittest.main()
