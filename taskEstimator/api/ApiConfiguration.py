import base64
import hashlib
import json


class RequestConfiguration:

    def __init__(self, url: str, method: str, headers: [], data: json) -> None:
        self.url = url
        self.method = method
        self.headers = headers
        self.data = data


class IApiConfiguration:
    def get_host(self) -> str:
        pass

    def get_auth_token_request_configuration(self, login: str, password: str) -> RequestConfiguration:
        return RequestConfiguration(
            f"{self.get_host()}/generateJWT",
            "POST",
            {
                'Content-Type': 'application/json'
            },
            ApiHelper.create_auth_object_for_user(login, password)
        )

    def get_list_data(self, auth_header: str, parameters_json_str: str) -> RequestConfiguration:
        return RequestConfiguration(
            f"{self.get_host()}/lists/parameters/{parameters_json_str}",
            "GET",
            {
                'Content-Type': 'application/json',
                'Authorization': auth_header
            },
            json.dumps({})
        )


class TestApiConfiguration(IApiConfiguration):
    HOST = "https://qa.bpower2.com/index.php/restApi"

    def get_host(self) -> str:
        return self.HOST


class ProductionApiConfiguration(IApiConfiguration):
    HOST = "https://b2ng.bpower2.com/index.php/restApi"

    def get_host(self) -> str:
        return self.HOST


class IApiDataConfiguration:
    def __init__(self, train_list_filters="", test_list_filters="") -> None:
        self.trainListFilters = train_list_filters
        self.testListFilters = test_list_filters

    def get_train_set_list_parameters(self) -> str:
        pass

    def get_test_set_list_parameters(self) -> str:
        pass


class DefaultApiDataConfiguration(IApiDataConfiguration):
    LIST_ID = 510
    PAGINATION = '{"page":1, "itemsPerPage": 0}'

    def get_train_set_list_parameters(self) -> str:
        return self._get_list_parameters(self.trainListFilters)

    def get_test_set_list_parameters(self) -> str:
        return self._get_list_parameters(self.testListFilters)

    def _get_list_parameters(self, list_filter="") -> str:
        if list_filter != "":
            return "{" + f'"listId": {self.LIST_ID}, "pagination":{self.PAGINATION}, "search": {list_filter}' + "}"

        return "{" + f'"listId": {self.LIST_ID}, "pagination":{self.PAGINATION}' + "}"


class ApiHelper:
    @staticmethod
    def create_auth_object_for_user(login: str, password: str) -> str:
        hash_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user_key = base64.standard_b64encode(f"{login}:{hash_pass}".encode("utf-8")).decode("utf-8")
        return json.dumps({
            "user-key": user_key
        })
