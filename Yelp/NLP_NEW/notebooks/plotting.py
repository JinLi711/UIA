"""
Plot graphs

"""

import pandas as pd
import matplotlib.pyplot as plt


def createplot(word_freq, name, save_file_name, threshold=0):
    """
    Creates plots based on word frequencies.
    Save plots.

    :param word_freq: keys are words and values are frequencies
    :type  word_freq: dict
    :param name: name of the plot
    :type  name: str
    :param save_file_name: file name to save plot
    :type  save_file_name: str
    :param threshold: cut off of frequency for word count.
                      If cutoff is not met, 
                      do not include the word in the plot.
    :type  threshold: int
    """

    df_occurences = pd.DataFrame({name: word_freq})
    plot = df_occurences[name].dropna()
    plot = plot[df_occurences[name] > threshold]
    plot.plot(kind="bar")
    plt.title(name)
    fig = plt.gcf()
    fig.set_size_inches(15, 8)
    plt.savefig(save_file_name, bbox_inches='tight')
    plt.show()