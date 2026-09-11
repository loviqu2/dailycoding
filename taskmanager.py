import unittest

#custom exceptions
class TaskNotFoundError(Exception):
    pass


class EmptyTaskNameError(Exception):
    pass


class TaskAlreadyDoneError(Exception):
    def __init__(self):
        super().__init__("This task has already been done.")


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

def log_action(func):  #func is whichever function is decorated
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"[LOG] {func.__name__} called")  #__name__ is the built in func that passes on any func automatically
            return result
        return wrapper


class PriorityTask(Task):
    def __init__(self, task_id, name, priority):
        #super() reuses the setup code, not the data, only save u from doing self.("") = ..., dont need to pass self in init anymore. and prio since it deal with parent param only
        super().__init__(task_id, name) #i need to reinsert the param of parent class, it can give acc to code only, not the id/name
        self.priority = priority


    # __str__ controls how an object looks when printed/str()'d; overriding it here lets PriorityTask show its extra priority attribute instead of Task's default format
    def __str__(self):  
        return f"[{self.task_id}] {self.name} ({self.status}) - Priority: {self.priority}"
        
print(PriorityTask(1, "Finish report", "High"))
        
t1 = Task(2, "Water plants")
t2 = PriorityTask(3, "Submit assignment", "High")
all_tasks = [t1, t2]

for task in all_tasks:
    print(task)

class TaskManager():
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    @log_action
    def add_task(self, name):
        if name.strip() == "" :
            raise EmptyTaskNameError("There is no input!")
        
        new_task = Task(self.next_id, name)
        self.tasks.append(new_task)
        self.next_id += 1

    @log_action
    def mark_done(self,task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                if task.status == "Done":
                    raise TaskAlreadyDoneError
                task.status = "Done"
                return 
        raise TaskNotFoundError(f"No task with id {task_id} found.")

    @log_action
    def remove_task(self,task_id):
        for task in self.tasks:
            if task.task_id == task_id:
              self.tasks.remove(task)
              return
        raise TaskNotFoundError(f"The task cannot be found for {task_id}")

    @log_action
    def get_pending(self):
        for task in self.tasks:
            if task.status == "pending": #pending has to be exact wording, we can use .lower() for future
                yield task
    
    @log_action
    def save_to_file(self, filename):
        with open(filename, "w") as f: 
            for task in self.tasks:
                f.write(f"{task.task_id},{task.name},{task.status} \n") #\n at the end is break line

    @log_action
    def load_from_file(self, filename):
        self.tasks = []
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                task_id = int(parts[0]) #parts[0] is just a string "1", need to int()
                name = parts[1]
                status = parts[2]
                new_task = Task(task_id, name, status)
                self.tasks.append(new_task)

            add_ids = [task.task_id for task in self.tasks] #list comprehension, for tasks in list of self.tasks, print(task.task_id)
            self.next_id = max(add_ids) + 1



        
        
    #unit testing

class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        m = TaskManager()
        m.add_task("Test task")
        self.assertEqual(len(m.tasks), 1)
        self.assertEqual(m.tasks[0].name, "Test task") #why use 0, is it because its the first?
        self.assertEqual(m.tasks[0].status, "pending")        
        
    def test_add_task_rejects_empty_name(self):
        m = TaskManager()
        with self.assertRaises(EmptyTaskNameError):
            m.add_task("")

    def test_mark_done(self):
        m = TaskManager()
        m.add_task("Test task")
        m.mark_done(1)
        self.assertEqual(m.tasks[0].status, "Done")

    def test_mark_done_missing_task_raise(self):  # dont need to do any add or wtv, we just wanna check with empty tasks
        m = TaskManager()
        with self.assertRaises(TaskNotFoundError):
            m.mark_done(999)      #why the value 999

    def test_mark_done_twice_raises(self):
        m = TaskManager()
        m.add_task("Test task")
        m.mark_done(1)
        with self.assertRaises(TaskAlreadyDoneError):
            m.mark_done(1)

    def test_remove_task(self):
        m = TaskManager()
        m.add_task("Test task")
        m.remove_task(1)
        self.assertEqual(len(m.tasks), 0)

    def test_remove_task_missing_raises(self):
        m = TaskManager()
        with self.assertRaises(TaskNotFoundError):
            m.remove_task(999)

    def test_get_pending(self):
        m = TaskManager()
        m.add_task("Test take")
        m.add_task("Test take 2")
        m.mark_done(1) #use (), not [], task id STARTS with 1, not 0
        pending = list(m.get_pending())
        self.assertEqual(len(pending), 1) #check the length of the pending list that only has one
        self.assertEqual(pending[0].name, "Test take 2") #check if the pending one is the exact test take, in this case t.t 2


unittest.main(argv=[""], exit=False)





#try, except only can print one outcome at a time, if you put two different add_task, it never reaches the 2nd
manager = TaskManager()

#test of add_task, p.s if i want to exclude this, i still need to do something like manager.add_task("Do something")
# task_names = ["", "Do homework", "Dont forget to take out trash"]

# for name in task_names:
#     try:
#         manager.add_task(name)
    
#     except ValueError as e:
#         print(f"Couldn't add task: {e}")
# manager.add_task("Doing 2nd thing")
# manager.add_task("Doing 3rd thing")
# print(manager.tasks)
# print(manager.next_id)

# #test of mark_done
# try:
#     manager.mark_done(1)
# except ValueError as e:
#     print(f"Couldn't mark task as done: {e}")


# try:
#     manager.mark_done(1)
# except ValueError as e:
#     print(f"Couldn't mark task as done: {e}")
    
# print(manager.tasks)

# #remove_task testing
# manager.remove_task(1)
# print(manager.tasks)

# #get_task testing
# for task in manager.get_pending():
#     print(task)

# manager.save_to_file("tasks.txt")
# manager.load_from_file("tasks.txt")


# new_manager = TaskManager()
# new_manager.load_from_file("tasks.txt")
# print(new_manager.tasks)
# print(new_manager.next_id)

# new_manager.add_task("Brand new task")
# print(new_manager.tasks)