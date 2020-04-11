import pandas as pd


def read_application_train_test_data(path_data="../data/"):
    """Function to read application data (train and test)
    Args:
        path_data: string, path to data
    Returns:
        df_app_train, df_app_test (pandas dataframes)
    """
    df_app_train = pd.read_csv(path_data+"application_train.csv")
    df_app_train.columns = [col.lower() for col in df_app_train.columns]

    df_app_test = pd.read_csv(path_data+"application_test.csv")
    df_app_test.columns = [col.lower() for col in df_app_test.columns]

    return df_app_train, df_app_test


def read_bureau_data(path_data="../data/"):
    """Function to read bureau data (main and balances)
    Args:
        path_data: string, path to data
    Returns:
        df_bureau, df_bureau_bal (pandas dataframes)
    """
    df_bureau = pd.read_csv(path_data+"bureau.csv")
    df_bureau.columns = [col.lower() for col in df_bureau.columns]

    df_bureau_bal = pd.read_csv(path_data+"bureau_balance.csv")
    df_bureau_bal.columns = [col.lower() for col in df_bureau_bal.columns]

    return df_bureau, df_bureau_bal


def read_credit_card_data(path_data="../data/"):
    """Function to read credit card data
    Args:
        path_data: string, path to data
    Returns:
        df_cc_bal (pandas dataframe)
    """
    df_cc_bal = pd.read_csv(path_data+"credit_card_balance.csv")
    df_cc_bal.columns = [col.lower() for col in df_cc_bal.columns]

    return df_cc_bal


def read_previous_application_data(path_data="../data/"):
    """Function to read data from previous applications
    Args:
        path_data: string, path to data
    Returns:
        df_prev_app (pandas dataframe)
    """
    df_prev_app = pd.read_csv(path_data+"previous_application.csv")
    df_prev_app.columns = [col.lower() for col in df_prev_app]

    return df_prev_app


def read_installment_payment_data(path_data="../data/"):
    """Function to read installment payment data
    Args:
        path_data: string, path to data
    Returns:
        df_installment_pay (pandas dataframe)
    """
    df_installment_pay = pd.read_csv(path_data+"installments_payments.csv")
    df_installment_pay.columns = [col.lower() for col in df_installment_pay]

    return df_installment_pay


def read_pos_cash_balance_data(path_data="../data/"):
    """Function to read installment payment data
    Args:
        path_data: string, path to data
    Returns:
        df_pos_cash_bal (pandas dataframe)
    """
    df_pos_cash_bal = pd.read_csv(path_data+"POS_CASH_balance.csv")
    df_pos_cash_bal.columns = [col.lower() for col in df_pos_cash_bal]

    return df_pos_cash_bal


def read_description(path_data="../data/"):
    """Function to read data description
    Args:
        path_data: string, path to data
    Returns:
        df_description (pandas dataframe)
    """
    df_description = pd.read_csv(path_data+"HomeCredit_columns_description.csv", encoding="ISO-8859-1")
    df_description.columns = [col.lower() for col in df_description]
    df_description.drop(columns="unnamed: 0", inplace=True)

    return df_description


def read_all_data(path_data="../data/"):
    """Function reads all data
    Args:
        path_data: string, path to data
    Returns:
        a, b, c (pandas dataframes)
    """
    df_app_train, df_app_test = read_application_train_test_data(path_data)
    df_bureau, df_bureau_bal = read_bureau_data(path_data)
    df_cc_bal = read_credit_card_data(path_data)
    df_prev_app = read_previous_application_data(path_data)
    df_installment_pay = read_installment_payment_data(path_data)
    df_pos_cash_bal = read_pos_cash_balance_data(path_data)
    df_description = read_description(path_data)
    return df_app_train, df_app_test, df_bureau, df_bureau_bal, \
           df_cc_bal, df_prev_app, df_installment_pay, df_pos_cash_bal, \
           df_description
