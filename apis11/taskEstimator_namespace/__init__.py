import json

import requests
from flask import request
from flask_restx import Namespace, Resource

from taskEstimator.ApiDataMapperMainClass import ApiDataMapper
from taskEstimator.dataCleaning.DataCleaner import NonEmptyClientAndProjectAndComplexityDataCleaner
from user_nn import PERSISTENCE
from apis11.taskEstimator_namespace.parametars import task_model_fields, task_model_fields1
import parser
from taskEstimator.DataframesNormalizeEvaluate import makeNormalizedTrainAndTestDataframes
from UserID import getUserID
from UserID import IDDictionary
from taskEstimator.ForwardBackwardPropagation import predict, predict_complexity, evaluate_algorithm, test_predictions, \
    back_propagation, evaluate_algorithm_with_bp
from taskEstimator.Split_Model_Predict import split_model_predict, split_model_predict_single_task

# defining namespace (Controller), namespace is group of requests which affect same data structures
api1 = Namespace('Completed Tasks', description='Completed tasks of the user')


# defining taskEstimator model
task_model1 = api1.model(
    'Completed Tasks',
    task_model_fields    # imported from /tasks.py
)

task_model2 = api1.model(
    'Uncompleted Tasks',
    task_model_fields1    # imported from /tasks.py
)



IDDictionary = {}


parser = api1.parser()
parser.add_argument('Authorization', type=str, location='headers', required=True)
parser.add_argument('taskid', type=str, location='args', required=False)
# route is url path to this resource for this particular example it's localhost:5000/tasks/
@api1.doc(parser=parser)
@api1.route("/singleTask")
class Task_Estimator1(Resource):
    @api1.doc('list_parametars')
    # telling swagger that response is in shape of task_model, it'll try to map the output to task_model definition
    @api1.marshal_list_with(task_model1)
    def get(self):
        if 'Authorization' in request.headers:
            dataCleaner = NonEmptyClientAndProjectAndComplexityDataCleaner(ApiDataMapper())
            headers = {
                'Authorization': request.headers['Authorization']  # <= use retrieved one!
            }

            getUserID(request.headers['Authorization'])
            if getUserID(request.headers['Authorization']) in IDDictionary.keys():
                trainedUserData = IDDictionary[getUserID(request.headers['Authorization'])]
            else:
                # this is for fetching all done tasks
                url = 'https://qa.bpower2.com/index.php/restApi/lists/parameters/{"listId":1039, "profile":1593}'
                payload = {}
                print("Estimated tasks are below!!!")
                allTasksResponse = requests.request("GET", url=url, headers=headers, data=payload)
                loads = json.loads(allTasksResponse.text)
                cleanedData = dataCleaner.clean_dataset(loads['default']['data'])
                normalizedTasksDataframe = makeNormalizedTrainAndTestDataframes(cleanedData)
                trainedUserData = split_model_predict(normalizedTasksDataframe)
                IDDictionary[getUserID(request.headers['Authorization'])] = trainedUserData

            # this is for fetching one task by id
            taskID = request.args['taskid']
            # PARAMS = {"listId": 900, "search": {"ProjectTask": {"id": "222175"}}}
            url1 = "https://qa.bpower2.com/index.php/restApi/lists/parameters/{\"listId\": 1039, \"search\": {\"ProjectTask\": {\"id\": \"%s\"}}}" % taskID
            print("The searched task is below!!!")
            r = requests.get(url=url1, headers=headers)
            loadedR = json.loads(r.text)
            cleanedR = dataCleaner.clean_dataset(loadedR['default']['data'])
            normalized_task_dataframe = makeNormalizedTrainAndTestDataframes(cleanedR)

            print(trainedUserData)
            print(normalizedTasksDataframe)

            return {
              'complexity': predict_complexity(trainedUserData, normalized_task_dataframe),
              'accuracy': '60%'
            }
        else:
            return "auth token not found", 401

        return \
            [{
                'task_id': 2345,
                'estimation': 2
            }]





parser1 = api1.parser()
parser1.add_argument('Authorization', type=str, location='headers', required=True)
@api1.doc(parser=parser1)
@api1.route("/unestimatedTasks")
class Task_Estimator2(Resource):
   @api1.doc('list_parametars')
   # telling swagger that response is in shape of task_model, it'll try to map the output to task_model definition

   @api1.marshal_list_with(task_model2)
   def get(self):
        if 'Authorization' in request.headers:
            dataCleaner = NonEmptyClientAndProjectAndComplexityDataCleaner(ApiDataMapper())
            headers = {
                'Authorization': request.headers['Authorization']  # <= use retrieved one!
            }

            # getUserID(request.headers['Authorization'])
            # if getUserID(request.headers['Authorization']) in IDDictionary.keys():
            #     trainedUserData = IDDictionary[getUserID(request.headers['Authorization'])]
            # else:
            #     # this is for fetching all done tasks
            #     #url = 'https://qa.bpower2.com/index.php/restApi/lists/parameters/{"listId":900, "profile":1118}'
            #     url = 'https://qa.bpower2.com/index.php/restApi/lists/parameters/{"listId":1039, "profile":1593}'
            #     payload = {}
            #     print("Estimated tasks are below!!!")
            #     allTasksResponse = requests.request("GET", url=url, headers=headers, data=payload)
            #     loads = json.loads(allTasksResponse.text)
            #     cleanedData = dataCleaner.clean_dataset(loads['default']['data'])
            #     normalizedTasksDataframe, targetVariable = makeNormalizedTrainAndTestDataframes(cleanedData)
            #     print(normalizedTasksDataframe)
            #     trainedUserData = split_model_predict(normalizedTasksDataframe, targetVariable)
            #     IDDictionary[getUserID] = trainedUserData

            # this is for fetching all done tasks
            # url = 'https://qa.bpower2.com/index.php/restApi/lists/parameters/{"listId":900, "profile":1118}'
            url = 'https://qa.bpower2.com/index.php/restApi/lists/parameters/{"listId":1039, "profile":1593}'
            payload = {}
            print("Estimated tasks are below!!!")
            allTasksResponse = requests.request("GET", url=url, headers=headers, data=payload)
            loads = json.loads(allTasksResponse.text)
            cleanedData = dataCleaner.clean_dataset(loads['default']['data'])
            normalizedTasksDataframe = makeNormalizedTrainAndTestDataframes(cleanedData)
            trainedUserData = split_model_predict(normalizedTasksDataframe)



            #this is for fetching all unestimated tasks
            url2 = 'https://qa.bpower2.com/index.php/restApi/lists/parameters/{"listId":1039, "profile":1595}'
            payload1={}
            print("Unestimated tasks are below!!!")
            unestimatedTasksResponse = requests.request("GET", url=url2, headers=headers, data=payload1)
            loads1 = json.loads(unestimatedTasksResponse.text)
            cleanedUnestimatedData = dataCleaner.clean_dataset(loads1['default']['data'])
            normalizesUnestimatedTasksDataframes = makeNormalizedTrainAndTestDataframes(cleanedUnestimatedData)
            trainedUnestimtedUserData = split_model_predict(normalizesUnestimatedTasksDataframes)



            l_rate = 0.3
            n_epoch = 500
            n_hidden = 2

            return {
              'complexity': evaluate_algorithm_with_bp(trainedUserData, normalizesUnestimatedTasksDataframes, back_propagation, l_rate, n_epoch, n_hidden),
              'accuracy': '60%'
            }
        else:
            return "auth token not found", 401

        return \
            [{
                'task_id': 2345,
                'estimation': 2
            }]
