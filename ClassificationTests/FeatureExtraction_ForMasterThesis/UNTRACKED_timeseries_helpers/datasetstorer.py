#!/usr/bin/env python
# coding: utf-8

# ## datasetstorer
# Use this function(s) to storer dataframes at the file system.

# In[ ]:


import pandas as pd


# In[2]:


def export_list_of_dataframes_to_csv(list_of_datasets,path):
    """Converts a given list of dataframes and converts it to a csv file to store on the given filesystem path.
    Export mechanism is made for the notation style of the smartPunch project.
    If changes are made here make shure to also change the import function(s)!

    Args:
        list_of_datasets (list): List object containing dataframe objects
        
        path (str in raw notation): Filepath including the filename and extension for the csv file to export. 
                                                            Make shure to use the raw representation to prevent error messages.
                                                            E.g.: 'r"C:\\Users\\tobia\\Downloads\\accdataset_periodMS2000_sampleUS1000.csv"'
                                                            
    Returns:
        void
    """
    pd.concat(list_of_datasets).to_csv(path);

