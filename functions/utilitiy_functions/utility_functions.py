import pandas as pd


def print_unique_char_values(pd_series, relative=True):
    if relative:
        print((round(pd_series.value_counts()/pd_series.shape[0]*100,1)).sort_values(ascending=False))
    else:
        print(pd_series.value_counts().sort_values(ascending=False))
