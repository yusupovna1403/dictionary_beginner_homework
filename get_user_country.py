def get_user_country(data:list, name:str) -> list:
    """
    Return the country of a user with a given name

    Args:
        data (dict): A dictionary of values
        name (str): The name of the user to search for
    Returns:
        str: The country of the user with the given name
    """
    for dict in data:
        if dict.get('name') == name:
            return dict.get('country')


data = [
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  }
]
name = "John"
print(get_user_country(data,name))