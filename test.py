#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from nasa_wildfires import get_modis, get_viirs_suomi, get_viirs_noaa, options


class NasaWildfiresUnitTest(unittest.TestCase):

    def test_modis(self):
        get_modis()
        for r in options.REGION_DICT.keys():
            get_modis(r)

    def test_viirs_suomi(self):
        get_viirs_suomi()
        for r in options.REGION_DICT.keys():
            get_viirs_suomi(r)

    def test_viirs_noaa(self):
        get_viirs_noaa()
        for r in options.REGION_DICT.keys():
            get_viirs_noaa(r)


if __name__ == '__main__':
    unittest.main()
