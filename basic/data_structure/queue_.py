# queue - means first in first out
from queue import Queue
# Creation:
# Creating a queue
my_queue = Queue()

# Enqueue (Insertion)
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

# Printing the queue
print("Queue:", my_queue.queue)

# Dequeue (Deletion)
removed_element = my_queue.get()
print("Removed element:", removed_element)

# Front (Peek)
front_element = my_queue.queue[0]
print("Front element:", front_element)
print(my_queue.queue[1])

# IsEmpty
is_empty = my_queue.empty()
print("Is empty:", is_empty)


'''
Queues are commonly used in scenarios such as task scheduling, handling requests in a web server, and managing resources in a computer system where tasks or processes need to be executed in a specific order. They are essential in ensuring fairness and order in the processing of elements.
'''


# Task Scheduling with queu 

import time

def process_task(task):
    print(f'processing task {task}')
    time.sleep(2)


# create task
    
task_queue = Queue()
task_queue.put('Task 1')
task_queue.put('Task 2')
task_queue.put('Task 3')

while not task_queue.empty():
    current_task = task_queue.get()
    process_task(current_task)

print('All tasks processed')