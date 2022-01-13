import os
from tinytag import TinyTag
from tune import Tune
import unittest
from tune_m4a import M4ATune


class TestM4ATune(unittest.TestCase):

    # https://stackoverflow.com/questions/1945920/why-doesnt-os-path-join-work-in-this-case
    def setUp(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        real_file_name_with_artwork = '06 Tuolumne.m4a'
        real_file_name_without_artwork = '01 There Are Maybe Ten Or Twelve.m4a'
        fake_file_name = 'random_fake_song.m4a'
        full_real_file_path_with_artwork = os.path.join(
            this_dir, real_file_name_with_artwork)
        full_real_file_path_without_artwork = os.path.join(
            this_dir, real_file_name_without_artwork)
        full_fake_file_path = os.path.join(this_dir, fake_file_name)
        self.real_m4a_with_artwork = M4ATune(full_real_file_path_with_artwork)
        self.real_m4a_without_artwork = M4ATune(
            full_real_file_path_without_artwork)
        self.fake_m4a = M4ATune(full_fake_file_path)

    def test_real_file_is_file(self):
        actual = self.real_m4a_without_artwork.is_file()
        expected = True
        self.assertEqual(actual, expected,
                         'Expected `is_file()` method to return `True`.')

    def test_fake_file_is_not_file(self):
        actual = self.fake_m4a.is_file()
        expected = False
        self.assertEqual(actual, expected,
                         'Expected `is_file()` method to return `False`.')

    def test_get_album(self):
        actual = self.real_m4a_without_artwork.get_album()
        expected = "Get Guilty"
        self.assertEqual(
            actual, expected, 'Expected `get_album() to return `Get Guilty`.')

    def test_get_artist(self):
        actual = self.real_m4a_without_artwork.get_artist()
        expected = "A.C. Newman"
        self.assertEqual(actual, expected,
                         'Expected `get_artist() to return `A.C. Newman`.')

    def test_create_search_term(self):
        actual = self.real_m4a_without_artwork.create_search_term()
        expected = "A.C. Newman Get Guilty Album Cover"
        self.assertEqual(
            actual, expected, 'Expected `create_search_term() to return `A.C. Newman Get Guilty Album Cover`.')

    def test_get_file_type(self):
        actual = self.real_m4a_without_artwork.get_file_type()
        expected = ".m4a"
        self.assertEqual(actual, expected,
                         'Expected `get_file_type() to return `.m4a`.')

    def test_has_album_artwork(self):
        actual = self.real_m4a_with_artwork.has_album_artwork()
        expected = True
        self.assertEqual(actual, expected,
                         'Expected `has_album_artwork() to return `True`.')

    def test_has_not_album_artwork(self):
        actual = self.real_m4a_without_artwork.has_album_artwork()
        expected = False
        self.assertEqual(actual, expected,
                         'Expected `has_album_artwork() to return `False`.')
