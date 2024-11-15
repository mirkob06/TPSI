import threading
import time

# Global event to signal the completion of the calculation
calculation_finished = threading.Event()

def perform_calculation():
    """Performs a heavy calculation (sum of numbers from 1 to 1,000,000)."""
    result = sum(range(1, 1000001))
    print(f"Calculation Result: {result}")

def display_status():
    """Shows a status update every 0.5 seconds while the calculation is running."""
    while not calculation_finished.is_set():
        print("Status: Working on the calculation...")
        time.sleep(0.5)

def run_threads():
    """Starts two threads: one for the calculation and another for status updates."""
    global calculation_finished
    
    # Create threads for calculation and status updates
    calc_thread = threading.Thread(target=perform_calculation)
    status_thread = threading.Thread(target=display_status)
    
    # Start both threads
    calc_thread.start()
    status_thread.start()
    
    # Wait for the calculation to complete
    calc_thread.join()
    calculation_finished.set()  # Signal that the calculation is done
    
    # Wait for the status thread to finish
    status_thread.join()
    print("All tasks completed.")

# Automatically run the threads when the script is executed
run_threads()
