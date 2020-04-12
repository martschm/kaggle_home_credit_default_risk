import sys
sys.path.append("../")

from functions.read_data import read_data
from functions.read_data import convert_column_names_types

import pandas as pd


def create_raw_dfs(path_data="../data/"):
    """This functions reads the data, converts column names and types
    and returns raw pandas dataframes
    Args:
        path_data: string, path to data
    Returns:
        df_a, df_b, df_c (pandas dataframes)
    """
    df_dict_orig = read_data.read_all_data(path_data)
    df_dict = convert_column_names_types.convert_column_names_types(df_dict_orig)
    
    df_app = pd.concat([df_dict["df_app_train"],df_dict["df_app_test"]], axis=0).reset_index(drop=True)
    df_bureau = df_dict["df_bureau"].reset_index(drop=True)
    df_bureau_bal = df_dict["df_bureau_bal"].reset_index(drop=True)
    df_cc_bal = df_dict["df_cc_bal"].reset_index(drop=True)
    df_prev_app = df_dict["df_prev_app"].reset_index(drop=True)
    df_installment_pay = df_dict["df_installment_pay"].reset_index(drop=True)
    df_pos_cash_bal = df_dict["df_pos_cash_bal"].reset_index(drop=True)
    df_target = df_dict["df_target"].reset_index(drop=True)
    
    return df_app, df_bureau, df_bureau_bal, df_cc_bal, \
           df_prev_app, df_installment_pay, df_pos_cash_bal, df_target
