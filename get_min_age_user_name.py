def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    lst = []
    for i in data:
        lst.append(i['age'])
    
    min = lst[0]
    i = 1
    for i in lst:
        if i < min:
            min = i
        
    for dict in data:
        if dict['age'] == min:
            return dict.get('name')
        
data = [
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  }, 
  {
    'name': 'Ban', 
    'age': 29
  }
]
print(get_min_age_user_name(data)) 