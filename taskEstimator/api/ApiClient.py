import requests
from taskEstimator.api.ApiConfiguration import *
from taskEstimator.Helpers import RunningMode


class IApiClient:

    def __init__(self, configuration: IApiConfiguration, login: str, password: str) -> None:
        self.configuration = configuration
        self.login = login
        self.password = password
        self.mode = RunningMode(RunningMode.NO_LOGS)

    def fetch_auth_token(self) -> json:
        pass

    def fetch_train_data(self, token: str, parameters: str) -> json:
        pass

    def fetch_test_data(self, token: str, parameters: str) -> json:
        pass

    def _print_log(self, log: str):
        if self.mode.is_loggable():
            print(f"LOG:\t{log}")


class ApiClient(IApiClient):

    def fetch_auth_token(self) -> json:
        request_data = self.configuration.get_auth_token_request_configuration(self.login, self.password)
        self._print_log(f"Executing:\n\t{request_data.method}: {request_data.url}\n\tH: [{request_data.headers}]")
        auth_response = json.loads(
            requests.request(
                request_data.method,
                request_data.url,
                headers=request_data.headers,
                data=request_data.data
            ).text
        )

        return auth_response

    def fetch_train_data(self, token: str, parameters: str) -> json:
        request_data = self.configuration.get_list_data(token, parameters)
        self._print_log(f"Executing:\n\t{request_data.method}: {request_data.url}\n\tH: [{request_data.headers}]")
        train_data_response = json.loads(
            requests.request(
                request_data.method,
                request_data.url,
                headers=request_data.headers
            ).text
        )

        return train_data_response

    def fetch_test_data(self, token: str, parameters: str) -> json:
        # it' the same request, just parameters are different, that why I could use prev method
        return self.fetch_train_data(token, parameters)
