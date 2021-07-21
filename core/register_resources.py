from auth.resource import register_auth_resources
from task.resource import register_task_resources


def register_resources(api):
    register_auth_resources(api)
    register_task_resources(api)
