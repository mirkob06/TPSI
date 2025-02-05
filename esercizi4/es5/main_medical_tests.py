import json
import os
from jsonschema import validate, ValidationError

def log_error(message):
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "error.log")
    with open(log_path, "a") as log_file:
        log_file.write(message + "\n")

def calculate_status(result_value, reference_range):

    try:
        lower_str, upper_str = reference_range.split('-')
        lower = float(lower_str)
        upper = float(upper_str)
    except Exception as e:
        # If parsing fails, return "unknown"
        return "unknown"
    
    if result_value < lower:
        return "troppo basso"
    elif result_value > upper:
        return "valore elevato"
    else:
        return "ok"

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(script_dir, "medical_tests.schema.json")
    json_path = os.path.join(script_dir, "medical_tests.json")

    # Load JSON schema
    try:
        with open(schema_path, "r") as sf:
            schema = json.load(sf)
    except Exception as e:
        error_message = f"Medical Tests: Error loading schema: {e}"
        log_error(error_message)
        print(error_message)
        return

    # Load JSON data
    try:
        with open(json_path, "r") as jf:
            data = json.load(jf)
    except Exception as e:
        error_message = f"Medical Tests: Error loading JSON file: {e}"
        log_error(error_message)
        print(error_message)
        return

    # Validate JSON data
    try:
        validate(instance=data, schema=schema)
    except ValidationError as ve:
        error_message = f"Medical Tests: JSON validation error: {ve.message}"
        log_error(error_message)
        print(error_message)
        return

    # Calculate and update status for each medical test record
    for test in data.get("medical_tests", []):
        try:
            # Convert result_value to a float
            result_value = float(test.get("result_value"))
            reference_range = test.get("reference_range")
            # Calculate status based on result_value and reference_range
            status = calculate_status(result_value, reference_range)
            test["status"] = status
        except Exception as e:
            error_message = f"Medical Tests: Error calculating status for record {test}: {e}"
            log_error(error_message)
            print(error_message)
            return

    print("Medical Tests: JSON data is valid and status updated:")
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
