import numpy as np

import pandas as pd

from matplotlib import pyplot as plt


def pie(data, title, dim = (10,4), loc = "center", anchor = None, ax = None, colors = None):

    if ax is None:
            fig, ax = plt.subplots(figsize = dim)
    else:
            ax.clear()

    if colors is None:
        ax.pie(data, labels = data)
    else:
        ax.pie(data, labels = data, colors = colors)

    if anchor is None:
        ax.legend(data.keys().tolist(), loc = loc)
    else:
        ax.legend(data.keys().tolist(), loc = loc, bbox_to_anchor = anchor)

    ax.set_title(title)

    return ax


def bar(x, y, xlab, ylab, dim = (16,9), title = None, color = "#1f77b4", ax = None):

    if ax is None:
        fig, ax = plt.subplots(figsize = dim)
    else:
        ax.clear()

    ax.bar(x = x, height = y, color = color)

    if title:
        ax.set_title(title, fontsize=20)

    ax.set_xlabel(xlab)

    ax.set_ylabel(ylab)

    return ax


def clean(df, rename_cols = None, drop_col = None, replace_val = None, val = None, to_str = None):

    if rename_cols:

        df.rename(columns = rename_cols, inplace=True)

    if to_str:
        df[f"{to_str}"] = df[f"{to_str}"].astype(str)

    if drop_col:
        df.drop(df.columns[drop_col], axis = 1, inplace = True)

    if replace_val and val:
        df.replace(to_replace = [replace_val], value = val, inplace = True)

    elif isinstance(replace_val, dict):
        df.replace(to_replace = replace_val, inplace = True)

    return df


def allele_rank(df, var):

    freq: pd.Series = df.groupby(f"{var}")[f"{var}"].count()

    freq = freq.sort_values(ascending = False)

    top_rank: pd.Series = freq[0:5]

    low_rank: pd.Series = freq[5:]

    freq = top_rank

    freq["Other"] = low_rank.sum()

    return freq


def LIN_prop(df, var):

    freq: pd.Series = df.groupby(f"{var}")[f"{var}"].count()

    prop: pd.Series = freq / freq.sum()

    prop_small: pd.Series = prop[prop <= 0.03]

    prop_final: pd.Series = prop[prop > 0.03]

    prop_final["Other"] = prop_small.sum()

    prop_final = round(prop_final, 3)

    return prop_final