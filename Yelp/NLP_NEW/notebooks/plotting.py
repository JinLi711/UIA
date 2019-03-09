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
    plt.xlabel("Key Words")
    plt.ylabel("Word Frequency Density")
    fig = plt.gcf()
    fig.set_size_inches(15, 8)
    plt.savefig(save_file_name, bbox_inches='tight')
    plt.show()


def plot_multi_level_bar_graph(df, save_file_name, threshold=0):
    """
    Creates plots based on word frequencies.
    Save plots.

    :param df: dataframe where each column is the neighborhood type
               index is the word
    :type  df: dataframe
    :param save_file_name: file name to save plot
    :type  save_file_name: str
    :param threshold: cut off of frequency for word count.
                      If cutoff is not met, 
                      do not include the word in the plot.
    :type  threshold: int
    """
    
    df.plot.bar(rot=0, figsize=(70,15))
    plt.savefig(save_file_name, bbox_inches='tight')
    plt.show()


class PlottingAttributes:
    """
    Class that contains the attributes for plotting.
    """

    def __init__(self, freq, title, save_fig_name):
        """
        :param freq: dictionary that map word to
                     its frequency
        :type  freq: dict
        :param title: title of plot
        :type  title: str
        :param save_fig_name: saved file name
        :type  save_fig_name: str
        """

        self.freq = freq
        self.title = title
        self.save_fig_name = save_fig_name

    def create_plot(self):
        createplot(
            self.freq,
            self.title,
            self.save_fig_name
        )