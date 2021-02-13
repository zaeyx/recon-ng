import unittest
import parsers


class TestParsers(unittest.TestCase):

  def test_parse_hostname_removes_schema(self):
    expected = "example.net"
    self.assertEqual(parsers.parse_hostname(
        "https://example.net"), expected)

  def test_parse_emails_returns_empty_list(self):
    expected = []
    self.assertEqual(parsers.parse_emails(''), expected)

  def test_parse_emails_returns_valid_email(self):
    expected = ["user@example.net"]
    self.assertEqual(parsers.parse_emails(
        'Looking for a person at user@example.net'), expected)

  def test_parse_names_returns_valid_name(self):
    expected = ("John", "J", "Smith")
    self.assertEqual(parsers.parse_name("John J Smith Jr."), expected)

if __name__ == '__main__':
    unittest.main()
