# For future troubleshooting

import unittest
from unittest import TestCase
import os
import sys
import pathlib
from pprint import pprint

import pandas as pd

from the_renamer import build_ids
from the_renamer import renamer

vax_raw = pd.read_csv('the_renamer/us_state_vaccinations.csv')

# Remove excess columns
vax = vax_raw.loc[:, ['date', 'location', 'people_fully_vaccinated_per_hundred']]
# Select the 12th of each month.
# str.endswith returns boolean series that is used to select
vax = vax.loc[vax['date'].str.endswith('-12'), :]
vax.reset_index(inplace=True, drop=True)
# Make columns to show renamer options. 
vax.loc[:, 'location_2'] = vax.loc[:, 'location']
vax.loc[:, 'location_3'] = vax.loc[:, 'location']

# Build Dictionaries 
one_name, many_names = build_ids('the_renamer/test_ids.csv')

vax_clean_state = renamer(vax, 'location', 'location', one_name, return_original=True
)
print(vax_clean_state['location'].unique())



vax_clean = renamer(vax, 'location', 'location', one_name, return_original=False, replacement_value='other'
)
print(vax_clean['location'].unique())
print(vax_clean_state['location'].unique())





print('h')