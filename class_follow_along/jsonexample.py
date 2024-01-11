import json



# Data dictionary to containing data
data_dictionary = {
    "numbers" : [24, 34, 45, 67, 89, 99, 69, 78, 32, 45], 
    "names" : ["Bob", "Betty", "James", "Katie", "Loser"], 
    "phone numbers" : [3334445555, 5553334444, 6667774444]
}

def sum_up(numbers):
    """Adds the numbers in a list"""
    total = 0 
    for n in numbers:
        total += n
    return total

def write_data_to_file(file_name, data):
    try:
        with open(file_name, "wt") as file_handle:
            json_data = json.dumps(data)
            file_handle.write(json_data)
    except FileNotFoundError:
        print(f"Unable to open the file: {file_name}")

def read_data_from_file(file_name):
    """read data from file_name and returns the dictionary"""
    try:
        with open(file_name, "rt") as file_handle:
            json_data = file_handle.read()
            dictionary_data = json.loads(json_data)
        return dictionary_data
    except FileNotFoundError:
        print(f"Could not open the file: {file_name}")
        return {}
        

def main():
    '''Main function to drive program'''
    # test
    # print(data_dictionary["numbers"])
    # print(data_dictionary["names"])
    # print(data_dictionary["phone numbers"])

    file_name = "jsonexample.json"
    write_data_to_file(file_name, data_dictionary)

    data = read_data_from_file(file_name)
    # test
    # print(data["numbers"])

main()