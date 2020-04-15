import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def barplot_badrate(df, col, target="target"):
    df = df.groupby(col).agg(
        applications = pd.NamedAgg(column=col, aggfunc="count"),
        bad_rate = pd.NamedAgg(column=target, aggfunc="mean")
    ).reset_index().sort_values(by="bad_rate")
    plt.figure(figsize=(15,5))
    plt.title(f"Applications & Bad-Rate -- '{col}'", fontsize=16)
    plt.bar(np.arange(df.shape[0]), df.applications.values, alpha=0.55)
    plt.xticks(np.arange(df.shape[0]), df[col].values, rotation=90, fontsize=12)
    plt.ylabel("Applications", fontsize=14, color="blue")
    ax2 = plt.twinx()
    ax2.plot(np.arange(df.shape[0]), df.bad_rate.values, color="red", marker="o", linewidth=3, markersize=7)
    ax2.set_ylabel("Bad-Rate", fontsize=14, color="red")
    ax2.grid(linestyle='--')
    plt.show()
