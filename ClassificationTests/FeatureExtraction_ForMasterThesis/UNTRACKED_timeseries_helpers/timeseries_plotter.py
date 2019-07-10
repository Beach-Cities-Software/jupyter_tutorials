#!/usr/bin/env python
# coding: utf-8

# ## plotting functions
# Helper functions to plot one or more dataset(s).

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


def universal_plotter_for_single_axis(list_of_datasets,
                                                                       list_of_axis_to_plot,
                                                                       list_of_dataset_legend_titles,
                                                                       plot_title, y_axis_label, x_axis_label,
                                                                       figSizeTupel = (20,10)):
    """Plots a specific axis of multiple datasets of an given array.
           Converting mechanism is made for the notation style of the smartPunch project.

    Args:
        list_of_datasets (list): List of datasets
        
        list_of_axis_to_plot (list): List of strings containig the axis to plot for the dataset of specific array index
    
        list_of_dataset_legend_titles (list): List strings containing the legend titles for each dataset axis.
        
        plot_title, y_axis_label , x_axis_label (str): Plot title, x and y plot axis labels
        
        figSizeTupel (tupel): Figure size
        
    Returns:
        void
    """   
    
    fig, ax = plt.subplots(figsize=figSizeTupel)

    idx = 0;
    for curDataSet in list_of_datasets:
        ax.plot(curDataSet['timestamp'].values,curDataSet[list_of_axis_to_plot[idx]], label=list_of_dataset_legend_titles[idx])
        idx+=1;
    
    ax.set(xlabel=x_axis_label, ylabel=y_axis_label,
           title=plot_title)
    ax.grid()
    plt.legend()
    plt.show()


# In[3]:


def universal_plotter_for_all_axis(list_of_datasets,
                                                                       list_of_dataset_legend_titles,
                                                                       plot_title, y_axis_label, x_axis_label,
                                                                       figSizeTupel = (20,10)):
    """Plots all axis of multiple datasets of an given array.
           Converting mechanism is made for the notation style of the smartPunch project.

    Args:
        list_of_datasets (list): List of datasets
        
        list_of_dataset_legend_titles (list): List strings containing the legend titles for each dataset axis.
        
        plot_title, y_axis_label , x_axis_label (str): Plot title, x and y plot axis labels
        
        figSizeTupel (tupel): Figure size
        
    Returns:
        void
    """
    
    fig, ax = plt.subplots(figsize=figSizeTupel)

    idx = 0;
    
    for curDataSet in list_of_datasets:
        universal_label = '%(titl)s (x-axis)'%{'titl': list_of_dataset_legend_titles[idx]} if list_of_dataset_legend_titles[idx] != '' else 'x-axis';
        ax.plot(curDataSet['timestamp'].values,curDataSet['x'], label=universal_label)
        universal_label = '%(titl)s (y-axis)'%{'titl': list_of_dataset_legend_titles[idx]} if list_of_dataset_legend_titles[idx] != '' else 'y-axis';
        ax.plot(curDataSet['timestamp'].values,curDataSet['y'], label=universal_label)
        universal_label = '%(titl)s (z-axis)'%{'titl': list_of_dataset_legend_titles[idx]} if list_of_dataset_legend_titles[idx] != '' else 'z-axis';
        ax.plot(curDataSet['timestamp'].values,curDataSet['z'], label=universal_label)
        idx+=1;
    
    ax.set(xlabel=x_axis_label, ylabel=y_axis_label,
           title=plot_title)
    ax.grid()
    plt.legend()
    plt.show()


# In[4]:


def single_plot_single_axis(dataset,axis ,plot_title, y_axis_label, x_axis_label, default_axis_legend=True,figSizeTupel = (20,10)):
    """Plots a single axis of a single dataset.
           Converting mechanism is made for the notation style of the smartPunch project.

    Args:
        dataset (dataframe): Dataset to plot
        
        axis (str): Axis to plot
    
        plot_title, y_axis_label , x_axis_label (str): Plot title, x and y plot axis labels
        
        default_axis_legend (str, default=True): If != true, the variable is used for the axis legend title instead of the default value
        
        figSizeTupel (tupel): Figure size
        
    Returns:
        void
    """   
    fig, ax = plt.subplots(figsize=figSizeTupel)
    
    universal_label = ' %(ax)s-axis'%{'ax': axis} if default_axis_legend == True else default_axis_legend;
    
    ax.plot(dataset['timestamp'].values,dataset[axis], label=universal_label)
    ax.set(xlabel=x_axis_label, ylabel=y_axis_label,
           title=plot_title)
    ax.grid()
    plt.legend()
    plt.show()


# In[ ]:


def single_plot_all_axis(dataset,plot_title, y_axis_label, x_axis_label,default_axis_legend=True,figSizeTupel = (20,10)):
    """Plots all axis of a single dataset.
           Converting mechanism is made for the notation style of the smartPunch project.

    Args:
        dataset (dataframe): Dataset to plot
        
        plot_title, y_axis_label , x_axis_label (str): Plot title, x and y plot axis labels
        
        default_axis_legend (list of str, default=True): If != true, the variable is used for the axis legend titles instead of the default values
        
        figSizeTupel (tupel): Figure size
        
    Returns:
        void
    """   
    fig, ax = plt.subplots(figsize=figSizeTupel)

    universal_label = 'x-axis' if default_axis_legend == True else default_axis_legend[0];
    ax.plot(dataset['timestamp'].values,dataset['x'], label=universal_label)
    universal_label = 'y-axis' if default_axis_legend == True else default_axis_legend[1];
    ax.plot(dataset['timestamp'].values,dataset['y'], label=universal_label)
    universal_label = 'z-axis' if default_axis_legend == True else default_axis_legend[2];
    ax.plot(dataset['timestamp'].values,dataset['z'], label=universal_label)
    
    ax.set(xlabel=x_axis_label, ylabel=y_axis_label,
           title=plot_title)
    ax.grid()
    plt.legend()
    plt.show()


# In[ ]:


def print_usage_info():
    print("use the functions in the notation of the following examples:")
    print("universal_plotter_for_single_axis([ds[0],...,ds[n]],['axisToPrintForDs1','axisToPrintForDsN'],['ds[0] legend text','ds[N] legend text'],'Plot-Title','y-Axis description','y-Axis description')")
    print("universal_plotter_for_all_axis([ds[0],...,ds[n]],['ds[0] legend text','ds[N] legend text'],'Plot-Title','y-Axis description','x-Axis description')")
    print("single_plot_single_axis(dataset,'axisToPrint','Plot-Title','y-Axis description','x-Axis description','default_axis_legend='legend text')")
    print("single_plot_all_axis(dataset,'Plot-Title','y-Axis description','x-Axis description','default_axis_legend='legend text')")

