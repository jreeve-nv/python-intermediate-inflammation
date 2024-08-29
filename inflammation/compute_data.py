"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views

class CSVDataSource:
    """
    Loads all the CSV files within a specified directory
    """
    def __init__(self, path):
        self.path = path

    def load_data(self):
        data_file_paths = glob.glob(os.path.join(self.path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No CSV files found in path {self.path}")
        data = map(models.load_csv, data_file_paths)
        return list(data)
    
class JSONDataSource:
    """
    Loads all the JSON files within a specified directory
    """
    def __init__(self, path):
        self.path = path

    def load_data(self):
        data_file_paths = glob.glob(os.path.join(self.path, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No JSON files found in path {self.path}")
        data = map(models.load_json, data_file_paths)
        return list(data)

def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    data = data_source.load_data()

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)
