Python Practice Notes
Quick reference — concept, one-line explanation, one example. Days 1–3 have no code (no notebook saved for those days).
Day 1 — Comprehensions
[i ** 2 for i in nums if i % 2 == 0]
Day 2 — Functions & basic OOP
Default/keyword args, __init__, self, mutating state.
Day 3 — Error handling
try:

    ...

except ValueError:

    ...

finally:

    ...

Raise where detected, catch where handled.
Day 4 — Context managers
with open("notes.txt", "w") as f:

    f.write("Hello file!")

class Announcer:

    def __enter__(self):

        print("Starting...")

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print("Finished.")

        return True   # suppresses the exception
Day 5 — Decorators
def loud(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return result

    return wrapper

@loud

def greet(name):

    return f"Hello, {name}"

*args = positional, **kwargs = keyword. Order matters: *args before **kwargs.
Day 6 — Generators
def count_forever():

    n = 1

    while True:

        yield n

        n += 1

Lazy, one value at a time. Much smaller memory footprint than a list.
Day 7 — Testing
import unittest

class TestSetAge(unittest.TestCase):

    def test_valid_age(self):

        self.assertEqual(set_age(25), 25)

    def test_negative_age_raises(self):

        with self.assertRaises(ValueError):

            set_age(-5)

unittest.main(argv=[''], exit=False)
Day 8 — Inheritance & super()
class Animal:

    def __init__(self, name):

        self.name = name

    def speak(self):

        return f"{self.name} makes a sound"

class Dog(Animal):

    def __init__(self, name, breed):

        super().__init__(name)   # runs Animal's full setup

        self.breed = breed

    def speak(self):             # overrides Animal's version

        return f"{self.name} says Woof!"

Child class checked first, then parent. Skipping super() silently skips whatever else the parent's __init__ does.
Day 9 — Polymorphism & composition
# Polymorphism: same call, different behavior per object

for animal in [Dog("Rex"), Cat("R.ball")]:

    print(animal.speak())

# Composition: "has-a", not "is-a"

class Car:

    def __init__(self, engine):

        self.engine = engine       # not inheriting from Engine

my_car = Car(Engine())

my_car.engine.start()              # dot-chain = composition

Inheritance = is-a, automatic parent updates, interchangeable subclasses. Composition = has-a, swappable parts, no forced hierarchy.
Day 9–10 — Custom exceptions
class TaskNotFoundError(Exception):

    def __init__(self, task_id):

        self.task_id = task_id

        super().__init__(f"No task with id {task_id}")

Raise inside the function that finds the problem, try/except at the call site. Lets you catch different failures separately and carry extra data (e.task_id), not just a message string.
Day 10 — Task Manager project upgrades
ValueError → TaskNotFoundError / EmptyTaskNameError / TaskAlreadyDoneError
Added PriorityTask(Task) with super().__init__() + overridden __str__
In progress: FileStorage class to pull save_to_file/load_from_file out of TaskManager (composition)
