import threading

# Shared variable and lock
shared_counter = 0
shared_lock = threading.Lock()

def increment_counter():
    """Each thread increments the shared counter 1000 times."""
    global shared_counter
    for _ in range(1000):
        with shared_lock:  # Lock the counter to ensure only one thread changes it at a time
            shared_counter += 1
    # After completing 1000 increments, print the counter value
    print(f"Thread completed 1000 increments. Current counter: {shared_counter}")

def manage_shared_resource():
    """Starts multiple threads to safely update the shared counter."""
    # Create a list of threads (10 threads, each will increment 1000 times)
    worker_threads = [threading.Thread(target=increment_counter) for _ in range(10)]
    
    # Start all threads
    for thread in worker_threads:
        thread.start()
    
    # Wait for all threads to finish
    for thread in worker_threads:
        thread.join()
    
    # Print the final value of the counter
    print(f"Final Counter Value: {shared_counter}")
    print("All threads finished updating the counter.")

# Run the program
manage_shared_resource()
