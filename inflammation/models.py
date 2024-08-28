"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.

Functions:
    load_csv - reads a CSV into a Numpy array
    daily_mean - returns the mean value of the input data
    daily_max - returns the maximum value of the input data
    daily_min - returns the minimum value of the input data
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    :returns: A 2D data array with inflammation data
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.
    
    :param data: A 2D array with inflammation data
        (each row contains measurements for a single patient across all days).
    :returns: An array of mean values of measurements for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.
    
    :param data: Numpy array
    :returns: An array of maximum values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.
    
    :param data: Numpy array
    :returns: An array of minimum values of measurements for each day.
    """
    return np.min(data, axis=0)
