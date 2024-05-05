import json

def read_storage(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{file_name}'.")
        return {}

def write_storage(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"Data written to '{file_name}' successfully.")