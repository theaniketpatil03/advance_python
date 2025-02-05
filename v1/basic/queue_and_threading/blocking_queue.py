'''

2. **Blocking Operations:**
   - The `queue` module provides blocking operations like `get` and `put`, which can be beneficial in concurrent programming. For example, if a thread attempts to dequeue from an empty queue (`get` operation) or enqueue to a full queue (`put` operation), it will block until the condition is satisfied. This can help in synchronization and coordination between threads.

'''

from queue import Queue
import threading
import time

def producer(queue, items):
    for item in items:
        print(f"Producing item: {item}")
        queue.put(item)
        time.sleep(1)  # Simulating time taken to produce an item

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break  # Exit the loop when a special item is encountered
        print(f"Consuming item: {item}")
        time.sleep(2)  # Simulating time taken to consume an item

# Creating a blocking queue
blocking_queue = Queue(maxsize=3)  # Setting a maximum size for demonstration

# Creating producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(blocking_queue, ['A', 'B', 'C', 'D']))
consumer_thread = threading.Thread(target=consumer, args=(blocking_queue,))

# Starting the threads
producer_thread.start()
consumer_thread.start()

# Waiting for the producer to finish
producer_thread.join()

# Adding a special item to signal the consumer to exit
blocking_queue.put(None)

# Waiting for the consumer to finish
consumer_thread.join()

print("All items produced and consumed.")

