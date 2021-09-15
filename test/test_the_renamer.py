import unittest
from unittest import TestCase
import os
import sys
import pathlib
from pprint import pprint

import pandas as pd

# TODO see if this is cross platform.
# Add functions the_renamer.py to system path.
test_full_path = pathlib.Path(__file__)
root_dir = test_full_path.parent.parent
main_dir = root_dir / ('the_renamer')
sys.path.insert(1, str(main_dir))

from the_renamer import base_clean
from the_renamer import build_ids
from the_renamer import renamer


class TestRenamer(TestCase):
    def setUp(self):
        test_file = 'test_us_state_vaccinations.csv'
        test_path = os.path.dirname(__file__)
        codes_dataframe = os.path.join(test_path, test_file)
        test_dataframe = pd.read_csv(codes_dataframe)
        cols_no_space = [
            'location'
        ]
        cleaned = base_clean(test_dataframe, cols_no_space=cols_no_space)
        cleaned.loc[:, '2nd_location'] = cleaned.loc[:, 'location']
        self.test_df = cleaned
        
        
        ids = os.path.join(test_path, 'test_ids.csv')
        # (Full name -> 2 letter abbreviation, 
        # many names -> 2 letter abbreviation)
        self.id_maps = build_ids(ids)
        
    def test_single_key_return_original(self):
        '''Test using dictionary built from 'single' column from ids.csv. 
        Returns original values for values not found in dictionary.'''
        renamed = renamer(
            self.test_df, 'location', 'location', self.id_maps[0])
        # Column verified by hand for test.
        validated_data = renamed.loc[:, 'test_abbr_no_replacement']
        the_same = renamed.loc[:, 'location'] == validated_data
        all_same = all(list(the_same))
        
        self.assertTrue(all_same)
        
    def test_many_keys_return_original(self):
        '''Test using dictionary built from 'many' column from ids.csv. 
        Returns original values for values not found in dictionary.'''
        # Tests reading and writing from different columns.
        renamed = renamer(
            self.test_df, 'location', '2nd_location', self.id_maps[1])
        # Same column reused since the same substitutions should have been made.
        validated_data = renamed.loc[:, 'test_abbr_no_replacement']
        the_same = renamed.loc[:, 'location'] == validated_data
        all_same = all(list(the_same))
        self.assertTrue(all_same)
    
    def test_many_keys_replacement(self):
        '''Test using dictionary built from 'many' column from ids.csv. 
        Returns 'non-state' for values not found in dictionary.'''
        renamed = renamer(
            self.test_df, 
            'location', 
            '2nd_location', 
            self.id_maps[1],
            return_original=False,
            replacement_value='non-state')
        
        validated_data = renamed.loc[:, 'test_abbr_replacement']
        the_same = renamed.loc[:, 'location'] == validated_data
        all_same = all(list(the_same))
        self.assertTrue(all_same)


if __name__ == '__main__':
    unittest.main()
    

# For adding more columns to the test file
'''
test_file = 'test_us_state_vaccinations_original.csv'
test_path = os.path.dirname(__file__)
codes_dataframe = os.path.join(test_path, test_file)
test_dataframe = pd.read_csv(codes_dataframe)
cols_no_space = [
            'location',
        ]
cleaned = base_clean(test_dataframe, cols_no_space=cols_no_space)
cleaned.loc[:, 'test_abbr_no_replacement'] = cleaned.loc[:, 'location']
cleaned.loc[:, 'test_abbr_replacement'] = cleaned.loc[:, 'location']
test_df = cleaned
ids = os.path.join(test_path, 'test_ids.csv')
id_maps = build_ids(ids)
test_df_2 = renamer(
            test_df, 'test_abbr_no_replacement', 'test_abbr_no_replacement', 
            id_maps[0]
            )
renamed = renamer(
            test_df_2, 'test_abbr_replacement', 'test_abbr_replacement', 
            id_maps[0], False, 'non-state'
            )
renamed.to_csv('test_us_state_vaccinations.csv')
'''
