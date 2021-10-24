# test fake file is not a file
# test fake file is a file
# test get album
# test get artist
# test create search term
# test get file type
from tinytag import TinyTag
from pathlib import Path
import mock
from mock import patch
from tune import Tune
import unittest
import sys
sys.path.append("./")


THIS_DIR = Path(__file__).parent

tune = THIS_DIR.parent / '06 Tuolumne.m4a'


class TestTune(unittest.TestCase):

    def test_is_file(self):
        self.assertEqual(tune.isfile, True)

    # # def setUp(self):
    # #     self.tune = Tune(
    # #         'Fake Song on the Bruce Springsteen Born to Run Album.m4a')

    # # @mock.patch('os.path.isfile')
    # # def test_not_file_is_not_file(self, mock_tune):
    # #     mock_tune.side_effect = False
    # #     assert self.tune.is_file() == "FAILED"

    # @mock.patch('project.classes.tune.Tune')
    # def test_class(self, mock_tune):

    #     class NewTune(file_path):
    #         def __init__(self, file_path_to_song):
    #             self.file_path_to_song = file_path_to_song

    #         def get_artist(self):
    #             return 'Bruce Springsteen'

    #         def get_album(self):
    #             pass

    #     new_tune = Tune("path/to/bruce/springsteen/born/to/run/jungleland.m4a")
    #     new_tune.artist = 'Bruce Springsteen'
    #     mock_get_artist.return_value = 'Bruce Springsteen'
    #     # mock_get_artist.assert_called()
    #     # mock_get_artist.assert_called_once_with('Bruce Springsteen')
    #     self.assertEqual(new_tune.get_artist, mock_get_artist.return_value)

    # # @patch('os.path.isfile')
    # # def test_file_is_file(self, mock_tune):
    # #     mock_tune.side_effect = True
    # #     assert self.tune.is_file() == "PASSED"

    # # @mock.patch('TinyTag.get(self.tune).album')
    # # def test_get_album_gets_the_album(self, mock_tune):
    # #     mock_tune.return_value = "Born to Run"
    # #     assert self.tune.get_album == "Born to Run"

    # # @mock.patch('TinyTag.get(self.tune).artist')
    # # def test_get_artist_gets_the_artist(self, mock_tune):
    # #     mock_tune.return_value = "Bruce Springsteen"
    # #     assert self.tune.get_artist == "Bruce Springsteen"

    # # def tearDown(self):
    # #     self.tune.dispose()


# import unittest
# from project.classes.tune import Tune


# class TestTune(unittest.TestCase):

#     @classmethod
#     def setUpClass(file):
#         pass

#     def test_is_file(self):
#         self.assertEqual(self.)
#         pass

#     def test_get_artist(self):
#         pass

#     def test_get_album(self):
#         pass

#     def test_create_search_term(self):
#         pass

#     def test_get_file_type(self):
#         pass

#     # test isfile
#     # test get_artist
#     # test get_album
#     # test create_search_term
#     # test get_file_type
