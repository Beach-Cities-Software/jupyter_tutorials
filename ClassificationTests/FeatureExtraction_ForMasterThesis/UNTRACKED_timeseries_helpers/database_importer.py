#!/usr/bin/env python
# coding: utf-8

# ## JSON Database representation of the raw data
# Helper functions to work with the dumped database file(s) in json representation.

# In[ ]:


import json
import pandas as pd
import datetime as datetime

# In[2]:


def jsonData_to_dataset_in_time_format(data):
    """Creates a list of dataframe objects from a given json object. Converts the timestamp col in datetime object format.
    Converting mechanism is made for the notation style of the smartPunch project.
    If changes are made here make shure to also change the export/import function(s)!

    Args:
        data (json): JSON Database representation dumped from mongoDB.
    
    Returns:
        list: List object containing the datasets as dataframe objects with timestamps in datetime object format.
    """

    the_cols = ['x','y','z','timestamp','label','hand','annotator']
    the_data = []
    
    for value in data:
        the_raws = []
        the_indxs = []
        idx = 0;
        cur_time = datetime.datetime.strptime(value['createdAt']['$date'],'%Y-%m-%dT%H:%M:%S.%fZ')
        for raw in value['raws']:
            micro = int(raw['timestamp'])/1000;
            raw_time = cur_time + datetime.timedelta(microseconds=micro);
            the_raws.append([raw['x'],raw['y'],raw['z'],int(raw_time),value['label'],value['hand'],value['annotator']])
            cur_time = raw_time;
            the_indxs.append(idx)
            idx += 1
        the_data.append(pd.DataFrame(the_raws,the_indxs,the_cols))
    return the_data


# In[13]:


#convert json data to dataframe list with timestamp in ms
def jsonData_to_dataset_in_timedifference_us(data):
    """Creates a list of dataframe objects from a given json object.Creates a list of dataframe objects from a given json object. Converts the timestamp col with relative timestamps in us. The last
        timestamp is the period time in ms.
    Converting mechanism is made for the notation style of the smartPunch project.
    If changes are made here make shure to also change the export/import function(s)!

    Args:
        data (json): JSON Database representation dumped from mongoDB.
    
    Returns:
        list: List object containing the datasets as dataframe objects with timestamps in 'since last timestamp' format.
    """
    
    the_cols = ['x','y','z','timestamp','label','hand','annotator']
    the_data = []
    
    for value in data:
        the_raws = []
        the_indxs = []
        idx = 0;
        raw_time_us = 0;
        for raw in value['raws']:
            raw_time_us += int(raw['timestamp'])/1000;
            the_raws.append([raw['x'],raw['y'],raw['z'],int(raw_time_us),value['label'],value['hand'],value['annotator']])
            the_indxs.append(idx)
            idx += 1
        the_data.append(pd.DataFrame(the_raws,the_indxs,the_cols))
    return the_data


# In[6]:


def import_local_json_database_file(filename):
    """Reads a json file from the file system and returns the json object representation of the file.
    Converting mechanism is made for the notation style of the smartPunch project.
    If changes are made here make shure to also change the export/import function(s)!

    Args:
        filename (str): JSON file containing the file extension. E.g. 'database.json'.
    
    Returns:
        json: JSON Object
    """
    
    #open json dataset
    with open(filename, 'r') as f:
        jsnDataset = json.load(f)
    return jsnDataset

