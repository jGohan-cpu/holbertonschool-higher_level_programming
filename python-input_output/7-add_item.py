import sys
import json

# Function to save Python object as JSON to a file


def save_to_json_file(my_obj, filename):
    """
    Save a Python object as JSON to a file.

    Args:
        my_obj (object): The object to be saved as JSON.
        filename (str): The name of the file to save the JSON data to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

# Function to load JSON data from a file and convert it to a Python object


def load_from_json_file(filename):
    """
    Load JSON data from a file and convert it to a Python object.

    Args:
        filename (str): The name of the file to load JSON data from.

    Returns:
        object: The Python object created from the JSON data.
    """
    with open(filename, 'r') as file:
        return json.load(file)


args = sys.argv[1:]

try:
    # Load existing list from file if it exists
    existing_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    # If the file doesn't exist, start with an empty list
    existing_list = []

# Add the new arguments to the existing list
existing_list.extend(args)

# Save the updated list to the file
save_to_json_file(existing_list, 'add_item.json')
