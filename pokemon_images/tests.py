# SPDX-FileCopyrightText: 2024 Tomodachi94 and contributors
#
# SPDX-License-Identifier: MIT

import unittest

import requests # Needed for testing that generated URLs return valid contents
import pokemon_images.__init__ as pokemon_images


class URLsTestCase(unittest.TestCase):
    """Tests for `pokemon_images.get_url_from_number`."""

    def test_generates_good_url(self):
        self.assertTrue(pokemon_images.get_url_from_number(1).startswith("https://") or
                        pokemon_images.get_url_from_number(1).startswith("http://"))

    def test_generates_good_status(self):
        """Ensure that the URLs generated as intended."""
        r = requests.get(pokemon_images.get_url_from_number(1))
        self.assertEqual(r.status_code, 200)

    def test_generates_good_content_type(self):
        """Ensure that the URLs generated as intended."""
        r = requests.get(pokemon_images.get_url_from_number(1))
        self.assertEqual(r.headers["content-type"], "image/png")


class RandomURLsTestCase(unittest.TestCase):
    """Tests for `pokemon_images.get_random_url`."""

    def test_generates_good_url(self):
        self.assertTrue(pokemon_images.get_random_url().startswith("https://") or
                        pokemon_images.get_random_url().startswith("http://"))

    def test_generates_good_status(self):
        """Ensure that the URLs generated as intended."""
        r = requests.get(pokemon_images.get_random_url())
        self.assertEqual(r.status_code, 200)

    def test_generates_good_content_type(self):
        """Ensure that the URLs generated as intended."""
        r = requests.get(pokemon_images.get_random_url())
        self.assertEqual(r.headers["content-type"], "image/png")

if __name__ == "__main__":
    unittest.main()
