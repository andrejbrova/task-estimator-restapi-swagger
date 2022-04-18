from pandas import DataFrame as df
from random import seed
import numpy as np
from sklearn.preprocessing import Normalizer

def makeNormalizedTrainAndTestDataframes(trainData):
    data_columns = ['Client', 'Project', 'Group', 'Complexity']      # and 'Complexity' should be added
    train_dataframe = df(columns=data_columns)
    train_target_variable = df(columns=['Complexity'])
    for index, data in enumerate(trainData):
        train_dataframe.loc[index] = [data.client, data.project, data.group, data.complexity]       # and data.complexity should be added
        train_dataframe = train_dataframe.astype('int')
        train_target_variable.loc[index] = [data.complexity]
        train_target_variable = train_target_variable.astype('int')
        # train_target_variable = np.ravel(train_target_variable)


    # test_dataframe = df(columns=data_columns)
    # test_target_variable = df(columns=['Complexity'])
    # for index, data in enumerate(testData):
    #     test_dataframe.loc[index] = [data.client, data.project, data.group, data.complexity]
    #     test_target_variable.loc[index] = [data.complexity]
    #     test_target_variable = test_target_variable.astype('int')
        #test_target_variable = np.ravel(test_target_variable)

    # Test Backprop on Seeds dataset
    seed(1)

    #dataf1 = Normalizer.fit_transform(train_dataframe)
    #dataf2 = Normalizer.fit_transform(train_target_variable)
    #normalizedTestDataframe = Normalizer().fit_transform(test_dataframe)
    dataf1 = Normalizer().fit_transform(train_dataframe)
    dataf2 = Normalizer().fit_transform(train_target_variable)

   #normalize input variables
    # if len(train_dataframe) == 1:
    #     dataf1 = Normalizer().fit_transform(train_dataframe)
    # else:
    #     if train_dataframe['Group'].max() == 0 and train_dataframe['Group'].min() == 0:
    #         columns_to_normalize = ['Client', 'Project', 'Complexity']
    #         train_dataframe = train_dataframe[columns_to_normalize].apply(
    #             lambda x: (x - x.min()) / (x.max() - x.min()) * 20)
    #         dataf1 = train_dataframe
    #     else:
    #         dataf1 = ((train_dataframe - train_dataframe.min()) / (train_dataframe.max() - train_dataframe.min())) * 20


    # trying to convert train dataframe into np array in order to successfully fit the model
    np_dataf1 = np.asarray(dataf1).astype(np.float32)
    np_dataf2 = np.asarray(dataf2).astype(np.float32)

    return np_dataf1