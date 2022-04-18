from taskEstimator.api.ApiDataMapper import IApiDataMapper


class ApiDataMapper(IApiDataMapper):
    GROUPS = {
            "_OTHER": 0,
            "API": 1,
            "Backend": 2,
            "Frontend": 3,
            "PHP": 4,
            "Cloud": 5,
            "SFA": 100,
            "Carlsberg": 101,
            "Grywalizacja": 102,
            "Gamification": 103
        }
    COMPLEXITY = {
        "EASY": 1,
        "MEDIUM": 2,
        "COMPLICATED": 3,
        "OVER-COMPLICATED": 4
    }
    #COMPLEXITY = {
     #   "": 1,
      #  "": 2,
       # "": 3,
        #"": 6
         #"": 9
          # "": 12
           # "": ++
    #}

    # the same will have to be made for Category, Group, Urgency, Type, Modul, Orderer


    def get_client_id(self, record: {}) -> int:
        try:
            print(record)
            return int(record['client']['id'])
        except ValueError:
            return 0

    def get_project_id(self, record: {}) -> int:
        try:
            return int(record['project']['id'])
        except ValueError:
            return 0

    def get_group(self, record: {}) -> int:
        tags = f'{record["task_name"]} {record["task_description"]}'
        for keyWord in self.GROUPS.keys():
            if keyWord in tags:
                return self.GROUPS[keyWord]

        return self.GROUPS["_OTHER"]

    def get_complexity(self, record: {}):
        try:
            execution_time = float(record["time_consumed"])
        except ValueError:
            execution_time = -1
        except TypeError:
            execution_time = -1

        if execution_time == -1:
            return 0
        elif execution_time <= 3.0:
            return self.COMPLEXITY["EASY"]
        elif execution_time <= 6.0:
            return self.COMPLEXITY["MEDIUM"]
        elif execution_time <= 12.0:
            return self.COMPLEXITY["COMPLICATED"]
        else:
            return self.COMPLEXITY["OVER-COMPLICATED"]

        #elif execution_time <= 1.0:
            #return self.COMPLEXITY[""]
        #elif execution_time <= 2.0:
            #return self.COMPLEXITY[""]
        #elif execution_time <= 3.0:
            #return self.COMPLEXITY[""]
        #elif execution_time <= 6.0:
            #return self.COMPLEXITY[""]
        #elif execution_time <= 9.0:
            #return self.COMPLEXITY[""]
        #elif execution_time <= 12.0:
            #return self.COMPLEXITY[""]
        #else:
            #return self.COMPLEXITY[""]


# will also need to add functions to get Category, Group, Urgency, Type, Modul, Orderer
    #def get_category(self, record: {}) -> int:
     #   try:
      #      return int(record['Category'])
       # except ValueError:
        #    return 0
    #def get_group(self, record: {}) -> int:
     #   try:
      #      return int(record['Group'])
       # except ValueError:
        #    return 0
    #def get_urgency(self, record: {}) -> int:
     #   try:
      #      return int(record['Urgency'])
       # except ValueError:
        #    return 0
    #def get_type(self, record: {}) -> int:
     #   try:
      #      return int(record['Type'])
       # except ValueError:
        #    return 0
    #def Modul(self, record: {}) -> int:
     #   try:
      # except ValueError:
       #     return 0
    #def get_orderer(self, record: {}) -> int:
     #   try:
      #      return int(record['Orderer'])
       # except ValueError:
        #    return 0


