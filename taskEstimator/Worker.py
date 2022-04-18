from taskEstimator.api.ApiClient import IApiClient
from taskEstimator.api.ApiConfiguration import IApiDataConfiguration
from taskEstimator.Helpers import RunningMode
from taskEstimator.dataCleaning.DataCleaner import IDataCleaner


class Worker:
    TRAIN_DATA = "trainDataSet"
    TEST_DATA = "testDataSet"

    def __init__(self, api_client: IApiClient, data_configuration: IApiDataConfiguration, data_cleaner: IDataCleaner, mode: RunningMode) -> None:
        self.mode = mode
        self.apiClient = api_client
        self.dataConfiguration = data_configuration
        self.dataCleaner = data_cleaner

        self.token = None
        self.trainData = None
        self.testData = None

        self.apiClient.mode = mode

    def work(self) -> {}:
        # self.__print_log("Fetching token...")
        # self.__fetch_auth_token()
        # self.__print_log(f"Token fetched: {self.token}")
        #
        # self.__print_log("Fetching train data...")
        # self.__fetch_train_data()
        # self.__print_log(f"Data fetched: {len(self.trainData)} records")

        self.__print_log(f"Cleaning data using: {type(self.dataCleaner)}...")
        self.trainData = self.dataCleaner.clean_dataset(self.trainData)
        self.__print_log(f"Data cleaned: {len(self.trainData)} records")

        self.__print_log("Fetching test data...")
        self.__fetch_test_data()
        self.__print_log(f"Data fetched: {len(self.testData)} records")

        self.__print_log(f"Parsing data...")
        self.testData = self.dataCleaner.parse_dataset(self.testData)
        self.__print_log(f"Data parsed: {len(self.testData)} records")

        return {
            self.TRAIN_DATA: self.trainData,
            self.TEST_DATA: self.testData
        }

    def __fetch_auth_token(self):
        auth_response = self.apiClient.fetch_auth_token()

        try:
            self.token = auth_response['token']
        except TypeError:
            print(auth_response)
            raise BaseException('Unauthorized')

    def __fetch_train_data(self):
        train_data_response = self.apiClient.fetch_train_data(
            self.token,
            self.dataConfiguration.get_train_set_list_parameters()
        )

        try:
            self.trainData = train_data_response['default']['data']
        except TypeError or KeyError:
            print(train_data_response)
            raise BaseException('Unknown data type')

    def __fetch_test_data(self):
        test_data_response = self.apiClient.fetch_test_data(
            self.token,
            self.dataConfiguration.get_test_set_list_parameters()
        )

        try:
            self.testData = test_data_response['default']['data']
        except TypeError or KeyError:
            print(test_data_response)
            raise BaseException('Unknown data type')

    def __print_log(self, log: str):
        if self.mode.is_loggable():
            print(f"LOG:\t{log}")
