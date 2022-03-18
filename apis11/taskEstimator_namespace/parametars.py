from flask_restx import fields

task_model_fields = {
    'accuracy': fields.String(required=True, description='Accuracy of the task'),
    'complexity': fields.Integer(required=True, description='Estimated complexity of task'),
}

task_model_fields1 = {
    'accuracy': fields.String(required=True, description='Accuracy of the task'),
    'complexity': fields.List(required=True, description='Estimated complexity of the unestimated tasks', cls_or_instance=fields.Integer),
}
