import asyncio

async def calculate_factorial(n):
    """Calculates the factorial of a number asynchronously."""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        await asyncio.sleep(0)  # Yield control to the event loop, allowing other tasks to run
    return result

async def async_factorials(numbers):
    """Calculates factorials asynchronously for a list of numbers."""
    tasks = [asyncio.create_task(calculate_factorial(num)) for num in numbers]
    results = await asyncio.gather(*tasks)  # Wait for all tasks to complete
    
    for num, res in zip(numbers, results):
        print(f"Factorial of {num} is {res}")

def exercise_4():
    """Runs asynchronous factorial calculations."""
    numbers = [5, 7, 10]  # Example numbers for factorial calculation
    asyncio.run(async_factorials(numbers))
    print("Exercise 4 completed.\n")

# Run the exercise
exercise_4()
