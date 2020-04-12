import numpy as np
import pandas as pd


def convert_column_names_types(df_dict_orig):
    """This function converts all column names and adds prefixes relating to
    dataset and column type
    Args:
        df_dict_orig: dictionary containing all dataframes
    Returns:
        df_dict: dictionary containing all dataframes with converted column names
    """

    df_dict = df_dict_orig.copy()

    df_dict["df_target"] = df_dict["df_app_train"][["sk_id_curr", "target"]].copy()
    df_dict["df_app_train"].drop(columns=["target"], inplace=True)

    df_dict["df_app_train"]["app_train_test"] = "train"
    df_dict["df_app_test"]["app_train_test"] = "test"

    exclude_cols = ["sk_id_curr", "sk_id_bureau", "sk_id_prev", "target", "app_train_test"]

    prefix = {
        "df_app_train": "app_",
        "df_app_test": "app_",
        "df_bureau": "bur_",
        "df_bureau_bal": "bur_bal_",
        "df_cc_bal": "cc_",
        "df_prev_app": "app_prev_",
        "df_installment_pay": "install_pay_",
        "df_pos_cash_bal": "pos_cash_",
        "df_target": "target_"
    }

    for k in df_dict.keys():

        df = df_dict[k].copy()

        # convert all numeric columns to float64
        int_cols = [col for col in df if df[col].dtype == "int64" and not col in exclude_cols]
        for col in int_cols:
            df[col] = df[col].astype("float64")

        # binary flags
        cols_bin_orig = [
            col for col in df
            if np.isin(df[col].dropna().unique(), [0, 1]).all()
               and not col in exclude_cols
        ]
        cols_bin_new = ["bin_" + col for col in cols_bin_orig]
        df.rename(dict(zip(cols_bin_orig, cols_bin_new)), axis=1, inplace=True)

        # numeric columns
        cols_num_orig = [
            col for col in df
            if not col.startswith("bin_")
               and df[col].dtypes in ["float64"]
               and not col in exclude_cols
        ]
        cols_num_new = ["num_" + col for col in cols_num_orig]
        df.rename(dict(zip(cols_num_orig, cols_num_new)), axis=1, inplace=True)

        # character columns
        cols_other_orig = [
            col for col in df
            if not col.startswith("bin_")
               and not col.startswith("num_")
               and not col in exclude_cols
        ]
        cols_other_new = ["char_" + col for col in cols_other_orig]
        df.rename(dict(zip(cols_other_orig, cols_other_new)), axis=1, inplace=True)
        
        # convert character columns with only two distinct values (yes,no) to binary
        bin_map = {"Y":1, "Yes":1, "y":1, "N":0, "No":0, "n":0}
        convert_to_bin = []
        cols = [col for col in df if "char_" in col]
        for col in cols:
            if np.isin(df[col].dropna().unique(), ["Y","N","Yes","No","y","n"]).all():
                convert_to_bin.append(col)
        if len(convert_to_bin)>0:
            for bin_col in convert_to_bin:
                df[bin_col.replace("char_","bin_")] = df[bin_col].map(bin_map)
                df.drop(columns=[bin_col], inplace=True)

        # add prefixes to columns
        all_cols_orig = [col for col in df if not col in exclude_cols]
        all_cols_new = [prefix[k] + col for col in all_cols_orig]
        df.rename(dict(zip(all_cols_orig, all_cols_new)), axis=1, inplace=True)

        # replace df in dict
        df_dict[k] = df

    return df_dict
