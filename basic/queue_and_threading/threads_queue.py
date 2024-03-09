import queue
import threading
import time



def process_task(thread, task_queue):
    while True:
        # Dequeue a task (blocking operation) - extract queue task

        current_task = task_queue.get() 
        if current_task is None: 
            break # stop the thread when None is encountered means if queue is empty
        

        print(f"**Processing task {thread}: {current_task}")
        time.sleep(2)


def main():

    # creating a thread-safe task queue

    task_queue = queue.Queue()

    # Creating and starting worker threads
    num_threads = 3

    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=process_task, args=(f"Thread-{i}", task_queue))    
        thread.start()
        threads.append(thread)

    # Enqueuing tasks
    for i in range(1,6):
        task_queue.put(f"Task {i}")

    # Adding None to signal threads to stop
    for _ in range(num_threads):
        task_queue.put(None)

    # Waiting for all threads to finish
    for thread in threads:
        thread.join()

    print("All tasks processed.")
    

if __name__ == "__main__":
    main()
