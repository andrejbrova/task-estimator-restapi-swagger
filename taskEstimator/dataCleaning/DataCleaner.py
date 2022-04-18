from taskEstimator.api.ApiDataMapper import IApiDataMapper


# also need to add: category, group, urgency, type, modul, orderer everywhere where needed

class CleanData:
    def __init__(self, client: int, project: int, group: int, complexity: int) -> None:
        self.client = client
        self.project = project
        self.group = group
        self.complexity = complexity
        # self.category = category
        # self.group = group
        # self.urgency = urgency
        # self.type = type
        # self.modul = modul
        # self.orderer = orderer

    def __str__(self) -> str:
        return "{" + \
               f'\n\t"client": {self.client},' \
               f'\n\t"project": {self.project},' \
               f'\n\t"group": {self.group},' \
               f'\n\t"complexity": {self.complexity}' + \
               "\n}"



class IDataCleaner:
    def __init__(self, data_map: IApiDataMapper) -> None:
        self.dataMap = data_map

    def parse_dataset(self, dataset: []) -> [CleanData]:
        pass

    def clean_dataset(self, dataset: []) -> [CleanData]:
        pass


class NonEmptyClientAndProjectAndComplexityDataCleaner(IDataCleaner):
    def parse_dataset(self, dataset: []) -> [CleanData]:
        cleaned = []
        for record in dataset:
            cleaned.append(
                CleanData(
                    self.dataMap.get_client_id(record),
                    self.dataMap.get_project_id(record),
                    self.dataMap.get_group(record),
                    self.dataMap.get_complexity(record)
                )
            )
        return cleaned

    def clean_dataset(self, dataset: []) -> [CleanData]:
        return self.__delete_records_with_no_client_or_project_or_complexity(
            self.parse_dataset(dataset)
        )

    @staticmethod
    def __delete_records_with_no_client_or_project_or_complexity(cleaned_data: [CleanData]) -> [CleanData]:
        valid_records = []
        for record in cleaned_data:
            if record.project != 0 and record.client != 0 and record.complexity != 0:
                valid_records.append(record)

        return valid_records
