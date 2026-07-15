import unittest
from backend import extract_text

class DummyMessage:
    def __init__(self):
        self.content = "Gemini Response"

class TestExtractText(unittest.TestCase):

    def test_extract_content(self):
        self.assertEqual(extract_text({"content": "Hello"}), "Hello")

    def test_extract_text_key(self):
        self.assertEqual(extract_text({"text": "Hi there"}), "Hi there")

    def test_extract_object_content(self):
        self.assertEqual(extract_text(DummyMessage()), "Gemini Response")

if __name__ == "__main__":
    unittest.main()
