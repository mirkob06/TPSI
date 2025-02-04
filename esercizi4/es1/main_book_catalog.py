import json
import os
from jsonschema import validate, ValidationError

def log_error(message):
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "error.log")
    with open(log_path, "a") as log_file:
        log_file.write(message + "\n")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(script_dir, "library_catalog.schema.json")
    json_path = os.path.join(script_dir, "library_catalog.json")

    # Load JSON schema
    try:
        with open(schema_path, "r") as sf:
            schema = json.load(sf)
    except Exception as e:
        error_message = f"Book Catalog: Error loading schema: {e}"
        log_error(error_message)
        print(error_message)
        return

    # Load JSON data
    try:
        with open(json_path, "r") as jf:
            data = json.load(jf)
    except Exception as e:
        error_message = f"Book Catalog: Error loading JSON file: {e}"
        log_error(error_message)
        print(error_message)
        return

    # Validate JSON data
    try:
        validate(instance=data, schema=schema)
    except ValidationError as ve:
        error_message = f"Book Catalog: JSON validation error: {ve.message}"
        log_error(error_message)
        print(error_message)
        return

    print("Book Catalog: JSON data is valid:")
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
