from api.ApiConfiguration import TestApiConfiguration, DefaultApiDataConfiguration
from api.ApiClient import ApiClient
from dataCleaning.DataCleaner import NonEmptyClientAndProjectAndComplexityDataCleaner
from Helpers import RunningMode
from Worker import Worker
from ApiDataMapperMainClass import ApiDataMapper
from taskEstimator.DataframesNormalizeEvaluate import makeNormalizedTrainAndTestDataframes


if __name__ == '__main__':
    # train_data_filter = '{"ProjectTask":{"performer":"szyszka", "status":30003219}}'
    # test_data_filter = '{"ProjectTask":{"performer":"szyszka", "status":30003385}}'
    #
    # worker = Worker(
    #     ApiClient(TestApiConfiguration(), "rafal.szyszka", "102938"),
    #     DefaultApiDataConfiguration(train_data_filter, test_data_filter),
    #     NonEmptyClientAndProjectAndComplexityDataCleaner(ApiDataMapper()),
    #     RunningMode(RunningMode.DEBUG)
    # )
    #
    # fetchedData = worker.work()
    # trainData = fetchedData[Worker.TRAIN_DATA]
    # testData = fetchedData[Worker.TEST_DATA]

    #makeNormalizedTrainAndTestDataframes(trainData)


    # data_columns = ['Client', 'Project', 'Group', 'Complexity']
    # train_dataframe = df(columns=data_columns)
    # train_target_variable = df(columns=['Complexity'])
    # for index, data in enumerate(trainData):
    #     train_dataframe.loc[index] = [data.client, data.project, data.group, data.complexity]
    #     train_target_variable.loc[index] = [data.complexity]
    #     train_target_variable = train_target_variable.astype('int')
    #     #train_target_variable = np.ravel(train_target_variable)
    #
    # test_dataframe = df(columns=data_columns)
    # test_target_variable = df(columns=['Complexity'])
    # for index, data in enumerate(testData):
    #     test_dataframe.loc[index] = [data.client, data.project, data.group, data.complexity]
    #     test_target_variable.loc[index] = [data.complexity]
    #     test_target_variable = test_target_variable.astype('int')
    #     #test_target_variable = np.ravel(test_target_variable)


# # Test Backprop on Seeds dataset
# seed(1)
#
# # normalize input variables
# minmax = dataset_minmax(train_dataframe)
# dataf = ((train_dataframe-train_dataframe.min())/(train_dataframe.max()-train_dataframe.min()))*20
# print(dataf)
#
# # trying to convert train dataframe into np array in order to successfully fit the model
# np_dataf = np.asarray(dataf).astype(np.float32)
#
# #split train dataset into train and test (70%-30%)
# train, test, trainTarget, testTarget = train_test_split(np_dataf, train_target_variable, train_size=0.7)
# train = np.asarray(train).astype(np.float32)
# test = np.asarray(test).astype(np.float32)
# trainTarget = np.asarray(train).astype(np.float32)
# testTarget = np.asarray(testTarget).astype(np.float32)

# evaluate algorithm
#l_rate = 0.3
#n_epoch = 500
#n_hidden = 2
#scores = evaluate_algorithm(dataf, back_propagation, n_folds, l_rate, n_epoch, n_hidden)
#scores = evaluate_algorithm(train, test, back_propagation, l_rate, n_epoch, n_hidden)
#print('Scores: %s' % scores)
#print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
