import unittest
from backend import extract_text

class DummyMessage:
    def __init__(self):
        self.content = "Gemini Response"

class TestExtractText(unittest.TestCase):

    def test_extract_content(self):
        msg = {"content": "Hello"}
        self.assertEqual(extract_text(msg), "Hello")

    def test_extract_text_key(self):
        msg = {"text": "Hi there"}
        self.assertEqual(extract_text(msg), "Hi there")

    def test_extract_object_content(self):
        msg = DummyMessage()
        self.assertEqual(extract_text(msg), "Gemini Response")

if __name__ == "__main__":
    unittest.main()
