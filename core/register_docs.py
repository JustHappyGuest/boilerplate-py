
from task.task_resource import register_task_docs
from auth.auth_resource import register_auth_docs

def register_docs(docs):
  register_auth_docs(docs)
  register_task_docs(docs)