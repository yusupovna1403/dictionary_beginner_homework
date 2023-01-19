def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    lst = []
    for i in data.values():
        if type(i)==int or type(i)==float:
            lst.append(i)
    
    max = lst[0]
    i = 1
    for i in lst:
        if i > max:
            max = i
    

    return max


data  = {
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  }
print(find_max_value(data))