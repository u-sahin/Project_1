import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_mixed_plot(dataframe, groupby, primary_measure, secondary_measure, title):
    """
    Description: This function can be used to create a plot with 2 measures

    Arguments:
        df: the dataframe
        group: columns to be grouped of the dataframe (can be multiple ones)
        primary_measure: the primary measure
        secondary_measure: the secondary measure (will be on the secondary_y axis)
        title: the title for the plot
        
    Returns:
        The plot
    """
    ax = dataframe.groupby(groupby)[secondary_measure].mean().plot(secondary_y=True, color="r", ylabel=primary_measure, rot=90, legend=True)
    dataframe.groupby(groupby)[primary_measure].mean().plot.bar(ylabel=secondary_measure, ax=ax, color='tab:blue', edgecolor="k", legend=True)
    
    plt.title(title)

    return plt


def create_mean_and_count_plot(dataframe, groupby, measure, secondary_ylabel, title):
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
    ax = dataframe.groupby(groupby).count().plot(secondary_y=True, color="r", ylabel=measure, rot=90, legend=False)
    dataframe.groupby(groupby)[measure].mean().plot.bar(ylabel=secondary_ylabel, ax=ax, color='tab:blue', edgecolor="k", legend=True)
    
    plt.title(title)

    return plt