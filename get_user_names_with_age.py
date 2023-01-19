def get_user_names_with_age(data:list, age:int) -> list:
    """
    Return a list of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        list: A list of users with the given age
    """
    lst = []
    for dict in data:
        if dict['age'] == age:
            lst.append(dict['name'])
    return lst  


data = [
  {
    'name': 'John', 
    'age': 30
  }, 
  {
    'name': 'Ann', 
    'age': 32
  }, 
  {
    'name': 'Sam', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 32
  }
]
age = 32
print(get_user_names_with_age(data,age))