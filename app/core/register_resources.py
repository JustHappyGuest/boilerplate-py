from app.auth.auth_resource import register_auth_resources
from app.task.task_resource import register_task_resources


def register_resources(api):
    register_auth_resources(api)
    register_task_resources(api)
