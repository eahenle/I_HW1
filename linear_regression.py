#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
%matplotlib inline

#import the dataset and Extract the Dependent and Independant variables
houses_data = pd.read_csv('housing_train.csv')
