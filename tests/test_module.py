from unittest.mock import patch
import unittest
# import budget
# from budget import

# https://realpython.com/python-mock-library/

# Need to work on this...


class UnitTests(unittest.TestCase):

    def test_create_search_term(song):
        with patch("__main__.TinyTag") as mock_tinytag:
            mock_tinytag.get.return_value.artist = "Bruce Springsteen"
            mock_tinytag.get.return_value.album = "Born to Run"
            assert create_search_term(
                "foo") == "Born to Run Bruce Springsteen Album Cover"


if __name__ == "__main__":
    unittest.main()
