from tune import Tune
import os
from tinytag import TinyTag
from project.classes.tune import Tune
import unittest


class TestTune(unittest.TestCase):

    # https://stackoverflow.com/questions/1945920/why-doesnt-os-path-join-work-in-this-case
    def setUp(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        real_file_name = '06 Tuolumne.m4a'
        fake_file_name = 'random_fake_song.m4a'
        full_real_file_path = os.path.join(this_dir, real_file_name)
        full_fake_file_path = os.path.join(this_dir, fake_file_name)
        self.tuolumne = Tune(full_real_file_path)
        self.fake = Tune(full_fake_file_path)

    def test_real_file_is_file(self):
        actual = self.tuolumne.is_file()
        expected = True
        self.assertEqual(actual, expected,
                         'Expected `is_file()` method to return `True`.')

    def test_fake_file_is_not_file(self):
        actual = self.fake.is_file()
        expected = False
        self.assertEqual(actual, expected,
                         'Expected `is_file()` method to return `True`.')

    def test_get_album(self):
        actual = self.tuolumne.get_album()
        expected = "Into the Wild (Music for the Motion Picture) [Deluxe Version]"
        self.assertEqual(
            actual, expected, 'Expected `get_album() to return `Into the Wild (Music for the Motion Picture) [Deluxe Version]`.')

    def test_get_artist(self):
        actual = self.tuolumne.get_artist()
        expected = "Eddie Vedder"
        self.assertEqual(actual, expected,
                         'Expected `get_artist() to return `Eddie Vedder`.')

    def test_create_search_term(self):
        actual = self.tuolumne.create_search_term()
        expected = "Eddie Vedder Into the Wild (Music for the Motion Picture) [Deluxe Version] Album Cover"
        self.assertEqual(
            actual, expected, 'Expected `create_search_term() to return `Eddie Vedder Into the Wild (Music for the Motion Picture) [Deluxe Version] Album Cover`.')

    def test_get_file_type(self):
        actual = self.tuolumne.get_file_type()
        expected = ".m4a"
        self.assertEqual(actual, expected,
                         'Expected `get_file_type() to return `.m4a`.')
