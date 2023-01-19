def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    
    lst = []
    for i in data.keys():
        if type(i)==int or type(i)==float:
            lst.append(i)
    
    max = lst[0]
    i = 1
    for i in lst:
        if i > max:
            max = i
    

    return max
data = {
    1: 'a', 
    2: 'b', 
    3: 'c'
  }
print(find_max_key(data))
 