class Task():
    #initializing parameter
    def __init__(self, task_id, name, status = "pending"): #default parameter just need =, == is for boolean.
        self.task_id = task_id
        self.name = name
        self.status = status

    def __str__(self): #help print the whole string, instead of just the object
        return f"[{self.task_id}] {self.name} ({self.status})"

    def __repr__(self):
        return self.__str__()

    #init does not need return

# t = Task(1, "Buy Groceries")
# print(t.task_id)
# print(t.name)
# print(t.status)

#create another class TaskManager, no need to init parameter as these are the things that 
#should start the exact same way.
class TaskManager():
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, name):
        if name.strip() == "" :
            raise ValueError("There is no input!")
        
        new_task = Task(self.next_id, name)
        self.tasks.append(new_task)
        self.next_id += 1

    def mark_done(self,task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                if task.status == "Done":
                    raise ValueError("The task is already marked as done")
                task.status = "Done"
                return 
        raise ValueError(f"No task with id {task_id} found.")

    def remove_task(self,task_id):
        for task in self.tasks:
            if task.task_id == task_id:
              self.tasks.remove(task)
              return
        raise ValueError(f"The task cannot be found for {task_id}")
        
        
            
            
        




#try, except only can print one outcome at a time, if you put two different add_task, it never reaches the 2nd
manager = TaskManager()

#test of add_task, p.s if i want to exclude this, i still need to do something like manager.add_task("Do something")
# task_names = ["", "Do homework", "Dont forget to take out trash"]

# for name in task_names:
#     try:
#         manager.add_task(name)
    
#     except ValueError as e:
#         print(f"Couldn't add task: {e}")

manager.add_task("Do 1")
manager.add_task("Doing 2nd thing")
manager.add_task("Doing 3rd thing")
# print(manager.tasks)
# print(manager.next_id)

#test of mark_done
# try:
#     manager.mark_done(1)
# except ValueError as e:
#     print(f"Couldn't mark task as done: {e}")


# try:
#     manager.mark_done(1)
# except ValueError as e:
#     print(f"Couldn't mark task as done: {e}")
    
# print(manager.tasks)


manager.remove_task(1)
print(manager.tasks)