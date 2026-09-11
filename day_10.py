#custom exceptions

class TaskNotFoundError(Exception):
    def __init__(self,task_id):
         self.task_id = task_id
         super().__init__(f"No task with {task_id}")


def find_task(task_id):
        if task_id != 1:
            raise TaskNotFoundError(task_id)
        return "Task Found"

    
try:
     print(find_task(2))

except TaskNotFoundError as e:
     print(e)
     print(e.task_id)