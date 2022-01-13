import os
from tinytag import TinyTag
from tune import Tune
import unittest
from tune_mp3 import MP3Tune


class TestMP3Tune(unittest.TestCase):

    # https://stackoverflow.com/questions/1945920/why-doesnt-os-path-join-work-in-this-case
    def setUp(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        real_file_name_with_artwork = '02 Best For Last (with artwork).mp3'
        real_file_name_without_artwork = '02 Best For Last (without artwork).mp3'
        fake_file_name = 'random_fake_song.m4a'
        full_real_file_path_with_artwork = os.path.join(
            this_dir, real_file_name_with_artwork)
        full_real_file_path_without_artwork = os.path.join(
            this_dir, real_file_name_without_artwork)
        full_fake_file_path = os.path.join(this_dir, fake_file_name)
        self.real_mp3_with_artwork = MP3Tune(full_real_file_path_with_artwork)
        self.real_mp3_without_artwork = MP3Tune(
            full_real_file_path_without_artwork)
        self.fake_mp3 = MP3Tune(full_fake_file_path)

    def test_real_file_is_file(self):
        actual = self.real_mp3_with_artwork.is_file()
        expected = True
        self.assertEqual(actual, expected,
                         'Expected `is_file()` method to return `True`.')

    def test_fake_file_is_not_file(self):
        actual = self.fake_mp3.is_file()
        expected = False
        self.assertEqual(actual, expected,
                         'Expected `is_file()` method to return `False`.')

    def test_get_album(self):
        actual = self.real_mp3_with_artwork.get_album()
        expected = "19"
        self.assertEqual(
            actual, expected, 'Expected `get_album() to return `19`.')

    def test_get_artist(self):
        actual = self.real_mp3_with_artwork.get_artist()
        expected = "Adele"
        self.assertEqual(actual, expected,
                         'Expected `get_artist() to return `Adele`.')

    def test_create_search_term(self):
        actual = self.real_mp3_with_artwork.create_search_term()
        expected = "Adele 19 Album Cover"
        self.assertEqual(
            actual, expected, 'Expected `create_search_term() to return `Adele 19 Album Cover`.')

    def test_get_file_type(self):
        actual = self.real_mp3_with_artwork.get_file_type()
        expected = ".mp3"
        self.assertEqual(actual, expected,
                         'Expected `get_file_type() to return `.mp3`.')

    def test_has_album_artwork(self):
        actual = self.real_mp3_with_artwork.has_album_artwork()
        expected = True
        self.assertEqual(actual, expected,
                         'Expected `has_album_artwork() to return `True`.')

    def test_has_not_album_artwork(self):
        actual = self.real_mp3_without_artwork.has_album_artwork()
        expected = False
        self.assertEqual(actual, expected,
                         'Expected `has_album_artwork() to return `False`.')
