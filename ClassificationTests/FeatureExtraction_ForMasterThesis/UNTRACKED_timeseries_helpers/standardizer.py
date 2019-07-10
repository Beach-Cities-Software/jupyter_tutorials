#!/usr/bin/env python
# coding: utf-8

# ## standardizer functions
# Helper functions to standardize/normate the dataset(s). 

# In[5]:


#interpolation modules
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline
from scipy.optimize import fmin

import pandas as pd
import numpy as np


# In[6]:


def normate_dataset_period(periodLengthInMS,samplingRateUS,dataset,interpolationKind= 'cubic'):
    """Normates the period of a given dataset list. Datasets in dataframe format! Stretches the periods with interpolation method choosen with the interpolationKind parameter. Default: Cubic.
    Converting mechanism is made for the notation style of the smartPunch project.

    Args:
        periodLengthInMS (str): Required period length in [ms] for each dataset
        
        samplingRateUS (str): Sampling rate in [us] for each datapoint.
    
        dataset (list): List of dataframe objects containing the datasets.
        
        interpolationKind (str): Interpolation method. Default: cubic.
        
    Returns:
        list: List object containing the interpolated datasets as dataframe objects with the stretched/compressed time period.
    """   

    # interpolated period length in us
    interp_period_us = periodLengthInMS*1000;
    
    #interpolated dataset array
    ds_interp = []

    # define cols for interp. dataset
    the_cols = ['x','y','z','timestamp','label','hand','annotator']
    
    #ds_interp = pd.DataFrame(dataset_raws_storer,np.arange(0,data_size,1),['x','y','z']);
    #print(ds_interp)

    dataset_numb = 0;
    
    # create and store the interpolation functions
    for ds_el in dataset:
        # original period length
        orig_period_length_us = ds_el['timestamp'][len(ds_el['timestamp'])-1]
        
        # stores the interpolating functions for each dataset element and axis
        f_x = (interp1d(ds_el['timestamp'].values,ds_el['x'],kind=interpolationKind,bounds_error=False,fill_value=(ds_el['x'][0],ds_el['x'][0])))
        f_y = (interp1d(ds_el['timestamp'].values,ds_el['y'],kind=interpolationKind,bounds_error=False,fill_value=(ds_el['y'][0],ds_el['y'][0])))
        f_z = (interp1d(ds_el['timestamp'].values,ds_el['z'],kind=interpolationKind,bounds_error=False,fill_value=(ds_el['z'][0],ds_el['z'][0])))
        
        # helper variables
        sample_moment = 0;

        # stores the interpolated raw data of the current dataset element as array(s)
        dataset_raws_storer = [];
        the_indxs = []
        idx = 0;
        
        # original period length is in intervall limit
        if orig_period_length_us <= interp_period_us:
            # interpolate x,y,z raw array of all elements in current dataset
            while sample_moment <= interp_period_us:
                dataset_raws_storer.append([f_x(sample_moment),f_y(sample_moment),f_z(sample_moment),int(sample_moment),ds_el['label'][0],ds_el['hand'][0],ds_el['annotator'][0]])
                sample_moment+= samplingRateUS;
                the_indxs.append(idx);
                idx+=1;
        else:
            #original interval is to long -> center data values and cut borders
            time_to_cutoff_on_each_side = round(((orig_period_length_us - interp_period_us)/2),0)
            #print('time_to_cutoff_on_each_side in us: {}'.format(time_to_cutoff_on_each_side))
            
            pseudo_sample_moment = time_to_cutoff_on_each_side;#round((time_to_cutoff_on_each_side/samplingRateUS),0)*samplingRateUS;
            #print('pseudo_sample_moment in us: {}'.format(pseudo_sample_moment))
            
            while sample_moment <= interp_period_us:
                dataset_raws_storer.append([f_x(pseudo_sample_moment),f_y(pseudo_sample_moment),f_z(pseudo_sample_moment),int(sample_moment),ds_el['label'][0],ds_el['hand'][0],ds_el['annotator'][0]])
                pseudo_sample_moment += samplingRateUS;
                sample_moment+= samplingRateUS;
                the_indxs.append(idx);
                idx+=1;
    
       # create a new interpolated dataset entry
        ds_interp.append(pd.DataFrame(dataset_raws_storer,the_indxs,the_cols))
        
    return ds_interp;


def change_strings_to_numbs(dataset):
    """Replaces the string values in the cols: hand, annotator and label with numbers.

    Args:
        dataset (list): List of dataframe objects containing the datasets.
        
    Returns:
        list: List object containing the datasets without any strings.
    """
    hands_dict = {'right':0,'left':1};
    annotator_keys = [];
    annotator_values = [];
    datasetList = [];
    
    idx = 0;
    for dataSet in dataset:
        datasetList.append(dataSet.copy(deep=True));
        # replace label
        datasetList[idx]['label'] = datasetList[idx]['label'].map({'no-action':0,'upper-cut':1,'hook':2,'frontal':3})
        
        # replace annotator-name
        datasetList[idx]['annotator'] = datasetList[idx]['annotator'].map(lambda s: s.lower());
        if datasetList[idx]['annotator'][0] not in annotator_keys:
            annotator_keys.append(datasetList[idx]['annotator'][0])
            annotator_values.append(len(annotator_values))
        
        # convert lists to dict
        dictionary = dict(zip(annotator_keys,annotator_values))
        datasetList[idx]['annotator'] = datasetList[idx]['annotator'].map(dictionary) 
        # replace hand
        datasetList[idx]['hand'] = datasetList[idx]['hand'].map(hands_dict)
        idx = idx +1;
    return datasetList