import os

import pandas as pd 


# Setting value for id csv. You cannot have any blank values in ids csv file. 
none_value = '<NONE>'
# All entries for id csv in many or single valued columns must be type string. 
# Entries for id csv in single valued columns may be any type. 

def base_clean(df, cols_no_space=None, format_headers=True):
    '''
    Data cleaning that I always apply to data when it is read in. 

    :param df:  (pd.DataFrame) Dataframe in.
    :param cols_no_space:  (list of strings) Column names for columns that will have spaces removed from beginning and end.
    :returns: (pd.DataFrame) Cleaned dataframe.
    '''
    if format_headers:
        # Changes columns from names 'NameLike THIS' to 'name_like_this'.
        df.columns = [
            str(c).strip().lower().replace(' ', '_') for c in df.columns
            ]
    # Remove spaces before and after all entries in columns.
    if cols_no_space != None:
        for col in cols_no_space:
            try: 
                df.loc[:, col] = df.loc[:, col].str.strip() 
            except: 
                print(
                    'Base data clean failed for column' + str(col))
    return df


def map_single_entry(
    df, code_column, desired_names, check_keys_unique=True,):
    '''
    Make dictionary with desired names as values and codes as keys. Each row in 
    code column has single value. 
    Args / Kwargs:
        df (pd.DataFrame): Dataframe in.
        cols_column (str): Column names for column that will be processed. 
        desired_names (pd.Series): Series of desired names with type row 
        removed. 
        check_keys_unique (boolean): Checks to make sure keys are 
        unique so don't get overwritten.  
    Returns:
        code_to_desired (dict): See first line.
    ''' 
    duplicate_keys = (
        code_column + ' values are not unique. Check id csv file.'
    )
    codes = df.loc[1:, code_column]
    if check_keys_unique:
        none_count = list(codes).count(none_value)
        gt_one_none = 1 if none_count >=1 else 0 
        len_codes_no_none = len(codes) - none_count
        len_set_codes_no_none = len(set(codes)) - gt_one_none
        assert len_codes_no_none == len_set_codes_no_none, duplicate_keys
    code_to_desired = {
        x: y  for x, y in zip(codes, desired_names) if x != none_value
        }
    
    return code_to_desired


def map_many_entries(df, code_column, desired_names, check_keys_unique=True):
    '''
    Make dictionary with desired names as values and codes as keys. Each row in 
    code column has many values. 
    Args / Kwargs:
        df (pd.DataFrame): Dataframe in.
        cols_column (str): Column names for column that will be processed. 
        desired_names (pd.Series): Series of desired names with type row 
        removed. 
        check_keys_unique (boolean): If True checks to make sure keys are 
        unique so don't get overwritten.  
    Returns:
        code_to_desired (dict): See first line.
    '''
    # Ignore categorization row.
    codes_raw = list(df.loc[1:, code_column])
    codes_all = []
    # Change list of strings to list of lists.
    for code_raw in codes_raw:
        # Make string into list.
        codes_list = code_raw.split(',')
        # Remove excess spaces. Remove empty strings generated by .split(). 
        codes_clean = [
            code.strip() for code in codes_list if code != ''
            ]
        codes_all.append(codes_clean)
    
    # Each code is a key and the desired name the value.
    code_to_desired = {}
    for desired_name, codes in zip(desired_names, codes_all):
        for code in codes:
            if check_keys_unique:
                duplicate_keys = (
                    str(code) + ' is not unique. Check id csv file.'
                    )
                assert code not in code_to_desired.keys(), duplicate_keys
            if code != none_value:
                code_to_desired[code] = desired_name 
    
    return code_to_desired


def build_ids(path_to_ids, check_keys_unique=True):
    '''
    Makes dictionaries for for all columns in ids csv file. 

    Args:
        path_to_ids (path or string): Csv file containing known names and \
            codes. Cannot have any blank entries. 
        check_keys_unique (boolean): Prevents duplicate keys from being \
            overwritten with last value.
    
    Returns:
        list of dicts: Same order as the codes in the ids csv. 
    '''
    df = pd.read_csv(path_to_ids)
    df = base_clean(
        df, cols_no_space=list(df.columns))

    # Find column label for destination.
    destination_col = df.loc[:, df.loc[0, :] == 'destination']
    # Check for multiple destination columns
    destination_label_message = 'You may have exactly one destination column.'
    assert destination_col.shape[1] == 1, destination_label_message
    destination_label = destination_col.columns[0]
    # Remove desination column
    df_reduced = df.loc[:, df.loc[0, :] != 'destination']
    name_mappings =[]
    # Not sure if this shold be list of DataFrame
    desired_names = df.loc[1:, destination_label]

    for header in list(df_reduced.columns):
        if df.loc[0, header] == 'single':
            single_map = map_single_entry(
                df, header, desired_names, check_keys_unique=check_keys_unique)
            name_mappings.append(single_map)
            
        elif df.loc[0, header] == 'many':
            many_map = map_many_entries(
                df, header, desired_names, check_keys_unique=check_keys_unique)
            name_mappings.append(many_map)
    return name_mappings 


def code_to_name(
    original_name, code, codes_dict, return_original, replacement_value):
    '''
    Map original name to new name.
    '''
    if return_original:
        if code in codes_dict.keys():
            return codes_dict[code]
        else :
            return original_name 
    else:
        if code in codes_dict.keys():
            return codes_dict[code]
        else :
            return replacement_value


def renamer(
    df, 
    rename_col, 
    code_col, 
    rename_dict, 
    return_original=True, 
    replacement_value=None):
    '''
    Renames column entries based on rename dictionary. 
    
    Args:
        df (pd.DataFrame): Dataframe in.
        rename_col (str): Name of column for entries to rename.
        code_col (str): Name of column for entries that will be used \
            identify the row. May be the same as rename_col.
        rename_dict (dict): Map from code_col value to rename_col new value. \
        return_original (bool): Whether to alter values not specified \
            in ids.csv, 
        replacement_value (any): If return_original equals False, value \
            to replace unspecified values.
    
    Returns:
        pd.DataFrame: Transformed dataframe.
    '''
    df.loc[:, rename_col] = list(map(
                code_to_name, 
                df.loc[:, rename_col],
                df.loc[:, code_col],
                [rename_dict] * df.shape[0],
                [return_original]* df.shape[0],
                [replacement_value]* df.shape[0]
                )) 

    return df 