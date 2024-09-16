import pandas as pandas

housing = pd.read_csv("data.csv")
#we have created a data frame in the above code
housing.head()#to show the first row in a limited count
housing.info()#to show the overview of the csv table
housing['CHAS'].value_counts()#it will the count of each group in the data
housing.describe()#to get the insights of your data
#understand the percentile, mean and standard deviation in the data

%matplotlib inline
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize = (20, 15))
#the above code will show all the features in the form of histogram

#we can do feature upscalling etc

import numpy as numpy
def split_train_test(data, test_ratio):