from flask_restx import Api

from apis11.taskEstimator_namespace import api1 as task_api_controller

# defining api metadata
api1 = Api(
    title="All Tasks Api",  # name
    version='0.0.1',  # version
    description='All Tasks Estimator api',   # description, the more you write here the better
    doc='/doc'  # path, from where the swagger documentation will be available, for me its: localhost:5000/doc
)

# adding some namespaces (controllers) to your API, checkout apis11/taskEstimator_namespace/__init__.py for more details
# added additional prefix /parametars to taskEstimator_namespace
api1.add_namespace(task_api_controller, path="/tasks/estimate")



#api1 = Api(
 #   title="One Task Api",  # name
  #  version='0.0.1',  # version
   # description='Single task Estimator api',   # description, the more you write here the better
    #doc='/doc1'  # path, from where the swagger documentation will be available, for me its: localhost:5000/doc
#)
#api1.add_namespace(task_api_controller, path='/tasks/estimate?id=')


