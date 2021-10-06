from unittest import TestCase
from mock import patch
import mock

import unittest
from artwork_grabber.helpers import create_search_term

# Accept a fake file name
# Return a string that represents what would actually be returned


class UnitTests(unittest.TestCase):
    def test_create_search_term(self):
        result = mock_tinytag_result
        with patch("__main__.TinyTag") as mock_tinytag:
            mock_tinytag.get.return_value.artist = "Bruce Springsteen"
            mock_tinytag.get.return_value.album = "Born to Run"
            assert create_search_term(
                "foo") == "Born to Run Bruce Springsteen Album Cover"
    # mock_tinytag.get.return_value.artist = "Bruce Springsteen"
    # # mock_tinytag.get.return_value.album = "Born to Run"
    # assert create_search_term(
    #     "foo") == "Bruce Springsteen Born to Run Album Cover"

    #     mock_song_info = {
    #         "album": "A Deeper Understanding",
    #         "artist": "The War On Drugs"
    #     }

    #     # patch where the function is USED, not where it is DEFINED
    #     @mock.patch('artwork_grabber.artwork_grabber.test.create_search_term', return_value=mock_song_info)
    #     def test_create_search_term(self, mock_song):
    #         actual_result = create_search_term(mock_song_info)
    #         expected_result = "A Deeper Understanding The War On Drugs Album Cover"
    #         self.assertEqual(actual_result, expected_result,
    #                          "Expected the search terms to match.")

    # if __name__ == "__main__":
    #     unittest.main()
