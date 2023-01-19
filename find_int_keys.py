def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    lst = []
    for i in data.keys():
        if type(i)==int:
            lst.append(i)

    return lst
data = {
    "x": "23",
    "3": "y", 
    "z": "5", 
    7:'a'
  }
print(find_int_keys(data))
    