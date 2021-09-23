from unittest import mock, TestCase
import unittest
from artwork_grabber.artwork_grabber import helpers


class UnitTests(TestCase):

    mock_song_info = {
        "album": "A Deeper Understanding",
        "artist": "The War On Drugs"
    }

    @mock.patch('artwork_grabber.artwork_grabber.TinyTag', return_value=mock_song_info)
    def test_create_search_term(self, mock_song):
        actual_result = helpers.create_search_term(mock_song_info)
        expected_result = "A Deeper Understanding The War On Drugs Album Cover"
        self.assertEqual(actual_result, expected_result,
                         "Expected the search terms to match.")

    # def test_create_search_term(self, mock_file_path_to_song):
        # def test_create_search_term(self):
        #     with patch("__main__.TinyTag") as mock_tinytag:
        #         mock_tinytag.get.return_value.artist = "Bruce Springsteen"
        #         mock_tinytag.get.return_value.album = "Born to Run"
        #         assert create_search_term(
        #             "foo") == "Born to Run Bruce Springsteen Album Cover"


if __name__ == "__main__":
    unittest.main()
