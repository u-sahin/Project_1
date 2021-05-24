import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_mixed_plot(df, group, measure, measure_2, title):
    """
    Description: This function can be used to create a plot with 2 measures

    Arguments:
        df: the dataframe
        group: columns to be grouped of the dataframe (can be multiple ones)
        measure: the first measure (will be on the secondary_y axis)
        measure_2: the second measure
        title: the title for the plot
        
    Returns:
        The plot
    """
    ax = df.groupby(group)[measure].mean().plot(secondary_y=True, color="r", ylabel=measure_2, rot=90, legend=True)
    df.groupby(group)[measure_2].mean().plot.bar(ylabel=measure, ax=ax, color='tab:blue', edgecolor="k", legend=True)
    
    plt.title(title)

    return plt


def create_mean_and_count_plot(df, group, measure, ylabel, title):
    """
    Description: This function can be used to create a plot with 1 measure and a count as a secondary_y axis

    Arguments:
        df: the dataframe
        group: columns to be grouped of the dataframe (can be multiple ones)
        measure: the measure
        ylabel: will be used as the secondary ylabes (for the count)
        title: the title for the plot
        
    Returns:
        The plot
    """
    ax = df.groupby(group).count().plot(secondary_y=True, color="r", ylabel=measure, rot=90, legend=False)
    df.groupby(group)[measure].mean().plot.bar(ylabel=ylabel, ax=ax, color='tab:blue', edgecolor="k", legend=True)
    
    plt.title(title)

    return plt